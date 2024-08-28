import importlib
import sys
import builtins
import operator

# Retrieve the first command-line argument and encode it
module_name = sys.argv[1]

# Import the module dynamically based on the encoded module name
module = importlib.import_module(module_name)

# Memoize frequently used names
getattr_func = builtins.getattr
getitem_func = operator.getitem
from_bytes_func = int.from_bytes
xor_func = operator.xor
add_func = operator.add
mod_func = operator.mod
truediv_func = operator.truediv
pow_func = operator.pow
mul_func = operator.mul
print_func = builtins.print
eq_func = operator.eq
all_func = builtins.all

# Perform various operations using the imported module and built-in functions
result = (
    getattr_func(module, sys.argv[1]) +
    from_bytes_func(b'big', sys.argv[1]) +
    xor_func(from_bytes_func(b'big', sys.argv[1]), add_func(add_func(3.3, 6.3), mod_func(10.0, 4.0))) +
    truediv_func(pow_func(11, 13), 10.0) +
    mul_func(pow_func(11, 13), 2, 4.0) +
    mod_func(mod_func(11.3, 3.4), 11.3) +
    pow_func(pow_func(11, 13), 65537, pow_func(11, 13)) == 497288852047669908918399061102224148238007014539217284516523697620389622574310368171
)

# Check if all values in the result tuple are True
is_all_true = all_func(result)

# Print the result
print_func(is_all_true)
