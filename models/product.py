class Product:
    def __init__(self, **kwargs):
        self.id = kwargs['id']
        self.name = kwargs['name']
        self.description = kwargs['description']
        self.value = kwargs['value']
        self.user_id = kwargs['user_id']
        self.created_at = kwargs['created_at']
        self.updated_at = kwargs['updated_at']
