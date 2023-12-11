import json

class Library:
    def __init__(self):
        try:
            with open("library.json", "r") as f:
                self.items = json.load(f)
        except FileNotFoundError:
            self.items = []

    def all(self):
        return self.items

    def get(self, id):
        return self.items[id]

    def create(self, data):
        data.pop('csrf_token')
        self.items.append(data)

    def save_all(self):
        with open("library.json", "w") as f:
            json.dump(self.items, f)

    def update(self, id, data):
        data.pop('csrf_token')
        self.items[id] = data
        self.save_all()

library = Library()
