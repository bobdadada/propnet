class Entity(object):
    _property = {}

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls, *args, **kwargs)
        instance._property = {}
        return instance
    
    def change_param(self, param, value):
        if param in dir(self):
            self._property[param] = [value, True]

    def change_params(self, **kwargs):
        for param, value in kwargs:
            self.change_param(param, value)
    
    def isParamChanged(self, param):
        if param not in self._property:
            return False
        elif self._property[param][1]:
            return False
        return True
    
    def areParamsChanged(self, params):
        for param in params:
            if self.isParamChanged(param):
                return True
        else:
            return False
    
    def get_param(self, param):
        if param in self._property:
            return self._property[0]
        else:
            return None
