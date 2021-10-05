from .equations import Equation1d
import sys
import numpy as np

class Solver1d:
    def __init__(self,equation):
        for key in equation.__dict__.keys():
            setattr(self,key,equation.__dict__[key])


        if self.scheme == 'fwd':
            self.step = self.fwd
        elif self.scheme == 'rk4':
            self.step = self.rk4
        else:
            sys.exit('err')

        
        self.flux_x = equation.flux_x
        self.actavite = equation.actavite

        self.u = equation.initial_data()
        self.u_n = np.zeros((self.Nt + 2,) + self.u.shape)
        self.u_n[0] = self.u

    
    def fwd(self,u,t):
        f = self.flux_x(u)
        activate = self.actavite(u,t)
        u = f - activate*self.dt_out
        return u


    def rk4(self,u,t):
        y = self.flux_x(u)
        #f = -self.actavite(u,t)
        h = self.dt_out

        K1 = -self.actavite(y , t)
        K2 = -self.actavite(y + h*0.5*K1 , t + h*0.5)
        K3 = -self.actavite(y + h*0.5*K2 , t + h*0.5 )
        K4 = -self.actavite(y + h*K3 , t + h )

        y_next = y + h/6*(K1 + 2*K2 + 2*K3 + K4)
        return y_next

    
    def solve(self):
        i = 0
        t = 0.0
        while t < self.t_final:
            i += 1
            dt = self.dt_out
            t += dt
            self.u = self.step(self.u,t)
            self.u_n[i,:] = self.u