# This is where the parameters are stored, along with the grid.
# One can solve different equations using the same setup.
# That's why this class definition is separate from Equation.

from dataclasses import dataclass

# 1d
@dataclass
class Pars1d:
    # Grid parameters
    t_final: float = 1.0
    dt_out: float = 0.05
    scheme: str = "fwd"  # now just could fwd(forward discrete)
