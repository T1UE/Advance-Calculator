from colorama import Fore
import time
import ctypes

RED = Fore.RED
BLUE = Fore.BLUE
YELLOW = Fore.YELLOW
CYAN = Fore.CYAN
L_YELLOW = Fore.LIGHTYELLOW_EX
WHITE = Fore.WHITE

functions = ["Basic Calculations","Matrix Calculations","Advanced Algebra","Calculus","Statistics and Probability","Vector Mathematics","Graphing Engine","Number Theory","Complex Mathematics","Linear Algebra - SUPER Advanced","Geometry","Differential Equations"]

for i in range(len(functions)):
    str_fn = functions[i]
    for j in range(len(str_fn)):
        if(i%2 == 0):
            print(f"{YELLOW}", end="")
        else:
            print(f"{L_YELLOW}", end="")
        print(str_fn[j], end="", flush=True)
        time.sleep(0.07)
    print()

    
def Basic_Calculations():
    pass

