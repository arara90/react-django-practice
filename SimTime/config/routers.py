class MultiRouter:
    db_map = {
        'db-todos': 'todos'
    }

    def __init__(self):
        print('routers ')

    def db_for_read(self, model, **hints):
        print('db_for_read:', model._meta.app_label)
        if(model._meta.app_label in self.db_map.values()):
            return 'db-' + model._meta.app_label
        else:
            return 'default'

    def db_for_write(self, model, **hints):
        print('db_for_write: ', model._meta.app_label)
        if(model._meta.app_label in self.db_map.values()):
            return 'db-' + model._meta.app_label
        else:
            return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        # print('here:                ', db, app_label, model_name)
        if (db in self.db_map.keys()):
            return app_label == self.db_map.get(db)

        else:
            return app_label not in self.db_map.values()
