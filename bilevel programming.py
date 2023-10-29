import pyomo.environ as pyo

opt=pyo.SolverFactory('scip')


#迭代法
#1:upper_level
# model=pyo.ConcreteModel()
# model.x=pyo.Var()
# model.y=pyo.Var()
#
# def cos1(model):
#     return -2*model.x+3*model.y<=12
# model.cons1=pyo.Constraint(rule=cos1)
#
# def cos2(model):
#     return model.x+model.y<=14
# model.cons2=pyo.Constraint(rule=cos2)
#
# def obj(model):
#     return -model.x-2*model.y
# model.obj=pyo.Objective(rule=obj,sense=pyo.minimize)
#
# opt.solve(model)
# print("目标函数为:{}".format(model.obj()))
# print("决策变量x的值为{}".format(model.x()))
# #print("决策变量y的值为{}".format(model.y()))

#1:lower_level
# model=pyo.ConcreteModel()
# model.y=pyo.Var()
# def cos1(model):
#     return -18+model.y<=-3
# model.cons1=pyo.Constraint(rule=cos1)
# def cos2(model):
#     return 18+model.y<=30
# model.cons2=pyo.Constraint(rule=cos2)
# def obj(model):
#     return -model.y
# model.obj=pyo.Objective(rule=obj,sense=pyo.minimize)
# opt.solve(model)
# print("目标函数为:{}".format(model.obj()))
# print("决策变量y的值为{}".format(model.y()))

#2
# import pyomo.environ as pyo
# opt=pyo.SolverFactory('scip')
# model=pyo.ConcreteModel()
# model.x=pyo.Var()
# def cos1(model):
#     return -2*model.x+36<=12
# model.cons1=pyo.Constraint(rule=cos1)
# def cos2(model):
#     return model.x+12<=14
# model.cons2=pyo.Constraint(rule=cos2)
# def obj(model):
#     return -model.x-2*12
# model.obj=pyo.Objective(rule=obj,sense=pyo.minimize)
# opt.solve(model)
# print("目标函数为:{}".format(model.obj()))
# print("决策变量x的值为{}".format(model.x()))


#通过KKT转为单层问题求解
model=pyo.ConcreteModel()
model.x=pyo.Var()
model.y=pyo.Var()
model.miu1=pyo.Var(domain=pyo.PositiveReals)
model.miu2=pyo.Var(domain=pyo.PositiveReals)

def cos1(model):
    return -2*model.x+3*model.y<=12
model.cons1=pyo.Constraint(rule=cos1)

def cos2(model):
    return model.x+model.y<=14
model.cons2=pyo.Constraint(rule=cos2)

def cos3(model):
    return model.miu1+model.miu2-1==0
model.cons3=pyo.Constraint(rule=cos3)

def cos4(model):
    return -3*model.x+model.y+3<=0
model.cons4=pyo.Constraint(rule=cos4)

def cos5(model):
    return 3*model.x+model.y-30<=0
model.cons5=pyo.Constraint(rule=cos5)

def cos6(model):
    return model.miu1*(-3*model.x+model.y+3)==0
model.cons6=pyo.Constraint(rule=cos6)

def cos7(model):
    return model.miu2*(3*model.x+model.y-30)==0
model.cons7=pyo.Constraint(rule=cos7)

def obj(model):
    return -model.x-2*model.y
model.obj=pyo.Objective(rule=obj,sense=pyo.minimize)

opt.solve(model)
print("目标函数为:{}".format(round(model.obj())))
print("决策变量x的值为{}".format(round(model.x())))
print("决策变量y的值为{}".format(round(model.y())))