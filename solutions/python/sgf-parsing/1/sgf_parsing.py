class SgfTree:
    def __init__(self, properties=None, children=None):
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other):
        if not isinstance(other, SgfTree):
            return False
        for key, value in self.properties.items():
            if key not in other.properties:
                return False
            if other.properties[key] != value:
                return False
        for key in other.properties.keys():
            if key not in self.properties:
                return False
        if len(self.children) != len(other.children):
            return False
        for child, other_child in zip(self.children, other.children):
            if child != other_child:
                return False
        return True

    def __ne__(self, other):
        return not self == other


class _Parser:
    def __init__(self, data: str):
        self.data = data
        self.i = 0
        self.n = len(data)

    def peek(self):
        """Return current char or None at end."""
        if self.i >= self.n:
            return None
        return self.data[self.i]

    def advance(self):
        """Consume one character."""
        ch = self.peek()
        if ch is not None:
            self.i += 1
        return ch

    def expect(self, ch):
        """Consume exactly `ch` or raise properties-without-delimiter error."""
        if self.peek() != ch:
            # used for bracket mismatches etc.
            raise ValueError("properties without delimiter")
        self.i += 1

    # ---------- Tree / node parsing ----------

    def parse_tree(self):
        """Parse a single tree: '(' node [node/variation...] ')' -> SgfTree."""
        if self.peek() != "(":
            raise ValueError("tree missing")

        self.expect("(")

        # After '(' we must see either ';' starting a node, or ')' meaning no nodes
        nxt = self.peek()
        if nxt != ";":
            # If we see ')', it's an empty tree: tree with no nodes
            if nxt == ")":
                raise ValueError("tree with no nodes")
            # Anything else isn't a valid node start
            raise ValueError("tree with no nodes")

        # First node = root
        root = self.parse_node()
        current = root

        while True:
            ch = self.peek()
            if ch == ";":
                # Sequential node in main line: child of current
                child = self.parse_node()
                current.children.append(child)
                current = child
            elif ch == "(":
                # Variation subtree: child of current, but current not advanced
                variation_root = self.parse_tree()
                current.children.append(variation_root)
            else:
                break

        if self.peek() != ")":
            # Missing closing paren for this tree
            raise ValueError("tree missing")
        self.expect(")")

        return root

    def parse_node(self):
        """Parse a node: ';' [props...] -> SgfTree."""
        self.expect(";")
        props = {}

        while True:
            key = self.parse_prop_ident()
            if key is None:
                break

            # key must be uppercase letters only
            if not key.isalpha() or not key.isupper():
                raise ValueError("property must be in uppercase")

            # At least one value must follow: must see '['
            if self.peek() != "[":
                raise ValueError("properties without delimiter")

            values = []
            while self.peek() == "[":
                values.append(self.parse_prop_value())

            props[key] = values

        return SgfTree(props)

    def parse_prop_ident(self):
        """Parse property identifier or return None if no ident at this point."""
        ch = self.peek()
        if ch is None or not ch.isalpha():
            # No property starts here
            return None

        start = self.i
        while self.peek() is not None and self.peek().isalpha():
            self.i += 1
        return self.data[start:self.i]

    # ---------- Property value parsing (SGF Text) ----------

    def parse_prop_value(self):
        """Parse SGF Text between '[' and ']' with SGF escaping rules."""
        self.expect("[")
        val_chars = []
        escaped = False

        while True:
            ch = self.peek()
            if ch is None:
                # Unterminated value
                raise ValueError("properties without delimiter")

            self.advance()

            if escaped:
                # After backslash:
                # - if whitespace: apply whitespace rules
                # - if non-whitespace: insert as-is
                if ch.isspace():
                    if ch == "\n":
                        # Escaped newline is removed
                        pass
                    else:
                        # Escaped non-newline whitespace becomes single space
                        val_chars.append(" ")
                else:
                    # Escaped non-whitespace inserted literally
                    val_chars.append(ch)
                escaped = False
            else:
                if ch == "\\":
                    escaped = True
                elif ch == "]":
                    break  # end of value
                else:
                    # Not escaped
                    if ch == "\n":
                        # Newline stays as newline
                        val_chars.append("\n")
                    elif ch.isspace():
                        # Any other whitespace -> space
                        val_chars.append(" ")
                    else:
                        val_chars.append(ch)

        return "".join(val_chars)


def parse(input_string):
    if not input_string:
        raise ValueError("tree missing")

    parser = _Parser(input_string)
    tree = parser.parse_tree()

    # After parsing one full tree, no extra junk allowed
    if parser.peek() is not None:
        raise ValueError("tree missing")

    return tree
