
# from pkg.pkg.pkg import module
from ssa.it.network import ssautil

ssautil.spam()

ssautil.toast()

# PYTHONPATH  (matches separator in PATH var)

#  windows -> separate with ;
#  non-windows -> separate with :
import sys

for folder in sys.path:
    print(folder)
