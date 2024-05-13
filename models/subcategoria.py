class Subcategory:
    def __init__(self, name, category_id, subcategory_id = None, created_at = None, updated_at = None):
        self.subcategory_id = subcategory_id
        self.name = name
        self.category_id = category_id
        self.created_at = created_at
        self.updated_at = updated_at

    def to_dict(self):
        return {
            "subcategory_id": self.subcategory_id,
            "name": self.name,
            "category_id": self.category_id,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            subcategory_id=data.get("subcategory_id"),
            name=data.get("name"),
            category_id=data.get("category_id"),
            created_at=data.get("created_at"),
            updated_at=data.get("updated_at")
        )