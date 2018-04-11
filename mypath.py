import os
class Path(object):
    @staticmethod
    def models_dir():
        return os.path.join(os.path.dirname(___file___), 'models/')
