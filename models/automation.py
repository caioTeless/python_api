class Automation:
    def __init__(self, **kwargs):
        self.id = kwargs['id']
        self.generation_date = kwargs['generation_date']
        self.transaction_id = kwargs['transaction_id']
        self.user_id = kwargs['user_id']
        self.created_at = kwargs['created_at']
        self.updated_at = kwargs['updated_at']
