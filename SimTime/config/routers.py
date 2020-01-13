class MultiRouter:
    def __init__(self):
        print('hi')
        self.model_list = ['leads', 'default']

    def db_for_read(self, model, **hints):
        print('db_for_read')
        if model._meta.app_label == 'leads':
            return 'leads'
        return 'default'

    def db_for_write(self,model,**hints):
        print('db_for_write')
        if model._meta.app_label == 'default':
            return 'default'
        return 'leads'

    def allow_relation(self, obj1, obj2, **hints):
        print('allow_relation')
        db_list = ('lead', 'default')
        if obj1._state.db in db_list and obj2._state.db in db_list:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        print(app_label)
        return True



# 실제 
# import random

# class PrimaryReplicaRouter:
#     def db_for_read(self, model, **hints):
#         """
#         Reads go to a randomly-chosen replica.
#         """
#         return random.choice(['replica1', 'replica2'])

#     def db_for_write(self, model, **hints):
#         """
#         Writes always go to primary.
#         """
#         return 'primary'

#     def allow_relation(self, obj1, obj2, **hints):
#         """
#         Relations between objects are allowed if both objects are
#         in the primary/replica pool.
#         """
#         db_list = ('primary', 'replica1', 'replica2')
#         if obj1._state.db in db_list and obj2._state.db in db_list:
#             return True
#         return None

#     def allow_migrate(self, db, app_label, model_name=None, **hints):
#         """
#         All non-auth models end up in this pool.
#         """
#         return True
