class Counter:
    def __init__(self, current=1, min_value=0, max_value=10):
        self.min_value = min_value
        self.max_value = max_value
        self.current = current
        self._verify_current()

    def _verify_current(self):
        if not (self.min_value <= self.current <= self.max_value):
            raise ValueError("Current value must be between min and max")

    def set_current(self, start):
        self.current = start
        self._verify_current()

    def set_max(self, max_max):
        if max_max < self.min_value:
            raise ValueError("Max cannot be less than min")
        self.max_value = max_max
        if self.current > self.max_value:
            self.current = self.max_value

    def set_min(self, min_min):
        if min_min > self.max_value:
            raise ValueError("Min cannot be greater than max")
        self.min_value = min_min
        if self.current < self.min_value:
            self.current = self.min_value

    def step_up(self):
        if self.current >= self.max_value:
            raise ValueError("Maximum reached")
        self.current += 1

    def step_down(self):
        if self.current <= self.min_value:
            raise ValueError("Minimum reached")
        self.current -= 1

    def get_current(self):
        return self.current

    def display(self):
        print(f"Counter value: {self.current} (min: {self.min_value}, max: {self.max_value})")

    def __str__(self):
        return f"Counter(value={self.current}, min={self.min_value}, max={self.max_value})"

counter = Counter()
counter.display()

counter.set_current(5)
counter.display()
counter.step_up()
print(counter)
