class User:
    def __init__(self, **kwargs):
        self.id = kwargs['id']
        self.name = kwargs['name']
        self.username = kwargs['username']
        self.email = kwargs['email']
        self.password = kwargs['password']
        self.password_confirmation = kwargs['password_confirmation']
        self.birthdate = kwargs['birthdate']
        self.active = kwargs['active']
        self.created_at = kwargs['created_at']
        self.updated_at = kwargs['updated_at']
