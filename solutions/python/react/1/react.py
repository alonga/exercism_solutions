class InputCell:
    def __init__(self, initial_value):
        self._value = initial_value
        self._dependents = []

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if self._value != new_value:
            self._value = new_value
            self._propagate()

    def _propagate(self):
        # Collect all impacted compute cells in update order
        queue = list(self._dependents)
        visited = set(queue)

        while queue:
            cell = queue.pop(0)
            cell._recompute()
            for dep in cell._dependents:
                if dep not in visited:
                    visited.add(dep)
                    queue.append(dep)

        # Now all values are final → trigger callbacks for all changed cells
        for cell in visited:
            if cell._value != cell._last_value:
                cell._last_value = cell._value
                for cb in list(cell._callbacks.values()):
                    cb(self._value)  # Call with *this* cell’s final stable value


class InputCell:
    def __init__(self, initial_value):
        self._value = initial_value
        self._dependents = []  # list of ComputeCell instances that depend on this cell

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        # If value doesn't change, nothing propagates, no callbacks
        if self._value == new_value:
            return
        self._value = new_value
        self._propagate()

    def _propagate(self):
        """
        Recompute all downstream ComputeCells until the system reaches
        a stable state, then call callbacks only on cells whose value
        actually changed.
        """
        # 1. Collect all affected compute cells via BFS
        queue = list(self._dependents)
        visited_list = []
        visited_set = set()

        while queue:
            cell = queue.pop(0)
            if cell in visited_set:
                continue
            visited_set.add(cell)
            visited_list.append(cell)
            queue.extend(cell._dependents)

        if not visited_list:
            return

        # 2. Iteratively recompute until we reach a fixed point
        # Start from current values
        new_values = {cell: cell._value for cell in visited_list}

        while True:
            changed = False
            for cell in visited_list:
                # compute using InputCell.value for inputs that are inputs
                # and new_values[...] for inputs that are ComputeCells
                vals = []
                for src in cell._inputs:
                    if isinstance(src, InputCell):
                        vals.append(src.value)
                    else:  # src is a ComputeCell
                        vals.append(new_values[src])
                new_val = cell._compute_fn(vals)
                if new_val != new_values[cell]:
                    new_values[cell] = new_val
                    changed = True
            if not changed:
                break  # reached stable state

        # 3. Commit new stable values and fire callbacks only where value changed
        for cell in visited_list:
            if new_values[cell] != cell._value:
                cell._value = new_values[cell]
                for cb in list(cell._callbacks.values()):
                    cb(cell._value)


class ComputeCell:
    def __init__(self, inputs, compute_function):
        self._inputs = inputs              # list of InputCell or ComputeCell
        self._compute_fn = compute_function
        self._dependents = []              # compute cells depending on this cell
        self._callbacks = {}

        # initial value from current inputs (they are already stable)
        self._value = self._compute_fn([c.value for c in self._inputs])

        # register reverse dependency
        for src in self._inputs:
            src._dependents.append(self)

    @property
    def value(self):
        return self._value

    def add_callback(self, callback):
        self._callbacks[id(callback)] = callback

    def remove_callback(self, callback):
        self._callbacks.pop(id(callback), None)
