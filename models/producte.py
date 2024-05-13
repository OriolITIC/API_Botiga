class Product:
    def __init__(self, name, description, company, price, units, subcategory_id,
                 product_id = None, created_at = None, updated_at = None):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.company = company
        self.price = price
        self.units = units
        self.subcategory_id = subcategory_id
        self.created_at = created_at
        self.updated_at = updated_at

    def to_dict(self):
        return {
            "product_id": self.product_id,
            "name": self.name,
            "description": self.description,
            "company": self.company,
            "price": self.price,
            "units": self.units,
            "subcategory_id": self.subcategory_id,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            product_id = data.get("product_id"),
            name = data.get("name"),
            description = data.get("description"),
            company = data.get("company"),
            price = data.get("price"),
            units = data.get("units"),
            subcategory_id = data.get("subcategory_id"),
            created_at = data.get("created_at"),
            updated_at = data.get("updated_at")
        )