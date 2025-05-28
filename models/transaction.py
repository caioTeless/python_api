class Transaction:
    def __init__(self, **kwargs):
        self.id = kwargs['id']
        self.date = kwargs['date']
        self.value = kwargs['value']
        self.description = kwargs['description']
        self.type = kwargs['type']
        self.user_id = kwargs['user_id']
        self.responsible = kwargs['responsible']
        self.category_id = kwargs['category_id']
        self.created_at = kwargs['created_at']
        self.updated_at = kwargs['updated_at']
        self.user_id = kwargs['user_id']
