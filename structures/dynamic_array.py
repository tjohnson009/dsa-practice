class DynamicArray:
    def __init__(self):
        self.stored = 0
        self.slots = [None, None, None, None]

    def __len__(self):
        return self.stored

    