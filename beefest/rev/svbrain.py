from z3 import *

ctx = Context()
v9 = Int('v9')
v10 = Int('v10')
 
constraints = [
    v10 % 10 == 1,
    v10 % 23 == 1,
    v10 % 3 == 0,
    v9 % 2 == 1,
    v9 % 21 == 9,
    v9 % 5 == 1,
    v10 / v9 > 1,
    And(v10>1),
    Or(v9 < 1, v9 > 99999999),
    Sum([v10 % 10 for _ in range(0, 100)]) == Sum([v9 % 10 for _ in range(0, 100)])  # Sum of digits is the same
]

solver = Solver()
solver.add(constraints)
if solver.check() == sat:
    model = solver.model()
    v9_value = model.evaluate(v9).as_long()
    v10_value = model.evaluate(v10).as_long()
    print(f"v9: {v9_value}, v10: {v10_value}")
    print(f"Length of v9: {len(str(v9_value))}")
    print(f"Length of v10: {len(str(v10_value))}")
