import errno
import os


# Tests patch this using @patch("paasio.super", ...)
class SuperStub:
    mock_object = None
    init_called = 0


super = SuperStub()


class MeteredFile:
    def __init__(self, file=None):
        super.init_called += 1
        self._file = file if file is not None else super.mock_object
        self._closed = False
        self._read_ops = 0
        self._read_bytes = 0
        self._write_ops = 0
        self._write_bytes = 0

    @property
    def read_ops(self): return self._read_ops

    @property
    def read_bytes(self): return self._read_bytes

    @property
    def write_ops(self): return self._write_ops

    @property
    def write_bytes(self): return self._write_bytes

    def _ensure_open(self):
        if self._closed:
            raise ValueError("I/O operation on closed file.")

    def read(self, size=None):
        self._ensure_open()
        data = self._file.read(size)

        # Always count read op
        self._read_ops += 1

        # Only count bytes if data received
        if data:
            self._read_bytes += len(data)

        return data

    def write(self, data):
        self._ensure_open()
        written = self._file.write(data)

        self._write_ops += 1

        # Count only bytes actually written (chunked)
        self._write_bytes += written

        return written

    # Iteration using readline()
    def __iter__(self):
        return self

    def __next__(self):
        self._ensure_open()
        line = self._file.readline()
        if not line:
            raise StopIteration
        self._read_ops += 1
        self._read_bytes += len(line)
        return line

    def __enter__(self):
        return self  # Do NOT call wrapped.__enter__

    def __exit__(self, exc_type, exc, tb):
        self._closed = True

        if hasattr(self._file, "__exit__"):
            suppress = self._file.__exit__(exc_type, exc, tb)
        else:
            suppress = False

        return suppress  # Suppress if wrapped chooses to


class MeteredSocket:
    def __init__(self, sock):
        self._sock = sock
        self._closed = False
        self._recv_ops = 0
        self._recv_bytes = 0
        self._send_ops = 0
        self._send_bytes = 0

    @property
    def recv_ops(self): return self._recv_ops

    @property
    def recv_bytes(self): return self._recv_bytes

    @property
    def send_ops(self): return self._send_ops

    @property
    def send_bytes(self): return self._send_bytes

    def _ensure_open(self):
        if self._closed:
            raise OSError(errno.EBADF, os.strerror(errno.EBADF))

    def recv(self, size, flags=0):
        if size is None:
            # Allow TypeError to propagate same as underlying object
            return self._sock.recv(size, flags)
        if not isinstance(flags, int):
            raise TypeError("integer is required")
        if not isinstance(size, int):
            raise TypeError("'NoneType' object cannot be interpreted as an integer")

        self._ensure_open()
        data = self._sock.recv(size, flags)

        if data:
            self._recv_ops += 1
            self._recv_bytes += len(data)

        return data

    def send(self, data, flags=0):
        if not isinstance(flags, int):
            raise TypeError("integer is required")

        self._ensure_open()
        sent = self._sock.send(data, flags)

        self._send_ops += 1

        # Count only bytes actually sent (chunked)
        self._send_bytes += sent

        return sent

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        self._closed = True

        if hasattr(self._sock, "__exit__"):
            suppress = self._sock.__exit__(exc_type, exc, tb)
        else:
            suppress = False

        return suppress
