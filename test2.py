import mycentpy
import numpy as np
import matplotlib.pyplot as plt


pars = mycentpy.Pars1d(t_final = 10.0,dt_out=0.01,scheme ='rk4')


class swag(mycentpy.Equation1d):
    def initial_data(self):
        u = np.zeros((1,2))
        u[0,1] = -0.5
        return u
    
    def flux_x(self,u):
        f= np.zeros_like(u)
        theta1 = u[:,0]
        theta2 = u[:,1]
        
        f[:,0] = theta1
        f[:,1] = theta2
        
        return f
    
    
    def actavite(self,u,t):
        a = np.zeros_like(u)
        omega = 2
        theta1 = u[:,0]
        theta2 = u[:,1]
        
        a[0,:] = -1*theta2
        a[:,1] = omega**2 * theta1
        
        return a 
    
eqn = swag(pars)
soln = mycentpy.Solver1d(eqn)
soln.solve()

plt.plot(soln.u_n[:,0,0],soln.u_n[:,0,1])
plt.title('position')
plt.xlabel(r'$\theta$')
plt.ylabel(r'$\frac{d\theta}{dt}$')
plt.show()