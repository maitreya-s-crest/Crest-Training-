class Person:
    def __init__(self, name, born, died=None):
        self.name = name
        self.born = born
        self.died = died
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def life_span(self):
        if self.died:
            return f"{self.born} - {self.died}"
        return f"Born {self.born}"

    def __str__(self):
        return f"{self.name} ({self.life_span()})"
