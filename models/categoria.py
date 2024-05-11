class Category:
    def __init__(self, name = str, category_id = None, created_at = None, updated_at = None):
        self.category_id = category_id
        self.name = name
        self.created_at = created_at
        self.updated_at = updated_at

    def to_dict(self):
        return {
            "category_id": self.category_id,
            "name": self.name,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
    @classmethod
    def from_dict(cls, data):
        return cls(
            category_id = data.get("category_id"),
            name = data.get("name"),
            created_at = data.get("created_at"),
            updated_at = data.get("updated_at")
        )