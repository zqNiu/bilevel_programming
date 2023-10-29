import pyomo.environ as pyo
from pao.pyomo import *
M = pyo.ConcreteModel()
M.x = pyo.Var()
M.y = pyo.Var()
M.o = pyo.Objective(expr=-M.x - 2*M.y, sense=pyo.minimize)
M.c1=pyo.Constraint(expr=-2*M.x+3*M.y<=12)
M.c2=pyo.Constraint(expr=M.x+M.y<=14)
M.sub = SubModel(fixed=M.x)
M.sub.o = pyo.Objective(expr=-M.y, sense=pyo.minimize)
M.sub.c1 = pyo.Constraint(expr=- 3*M.x + M.y <= -3)
M.sub.c2 = pyo.Constraint(expr=3*M.x + M.y <= 30)


opt = Solver("pao.pyomo.FA", mip_solver="scip")
results = opt.solve(M)
M.y.pprint()
M.x.pprint()
print(M.o())