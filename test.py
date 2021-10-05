import mycentpy 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

pars = mycentpy.Pars1d(
    t_final = 1.0,
    dt_out = 0.05,
    scheme = 'fwd'
)



class nonliner(mycentpy.Equation1d):
    def initial_data(self):
        u = np.zeros((1,2))
        return u
    
    def flux_x(self,u):
        f = np.zeros_like(u)
        theta1 = u[:,0]
        theta2 = u[:,1]
        
        f[:,0] = theta1
        f[:,1] = theta2
        return f
    
    def actavite(self,u,t):
        a = np.zeros_like(u)
        Q = 1.0
        F = 1.0
        omu = 1.5
        theta1 = u[:,0]
        theta2 = u[:,1]
        
        a[:,0] = -1 * theta2
        a[:,1] = 1 / Q * theta2 + np.sin(theta1) - F * np.cos(omu*t)
        return  a
    
eqn = nonliner(pars)
soln = mycentpy.Solver1d(eqn)
soln.solve()


plt.plot(soln.u_n[:,0,0],soln.u_n[:,0,1])
plt.show()