# This is the equation class including all equation-specific definitions.

import numpy as np
from abc import ABC, abstractmethod
from .parameters import Pars1d

# 1d
class Equation1d(ABC, Pars1d):
    def __init__(self, pars):
        for key in pars.__dict__.keys():
            setattr(self, key, pars.__dict__[key])
        self.Nt = int(np.ceil(self.t_final / self.dt_out))
        

    @abstractmethod
    def initial_data(self):
        pass

    @abstractmethod
    def flux_x(self, u):
        pass

    @abstractmethod
    def actavite(self, u,t):
        pass
