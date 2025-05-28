class Configuration:
    def __init__(self, **kwargs):
        self.id = kwargs['id']
        self.type = kwargs['type']
        self.description = kwargs['description']
        self.active = kwargs['active']
        self.user_id = kwargs['user_id']
        self.created_at = kwargs['created_at']
        self.updated_at = kwargs['updated_at']
