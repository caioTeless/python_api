from controllers.base_controller import BaseController

class UsersController:
    def __init__(self):
        self.base = BaseController('users')
        
    def add(self):
        return self.base.add()

    def get_all(self):
        return self.base.get_all()

    def get(self, id):
        return self.base.get(id)

    def update(self, id):
        return self.base.update(id)

    def delete(self, id):
        return self.base.delete(id)