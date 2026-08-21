from colorama import Fore
import time
import ctypes
import references
from Basic.basic_parse import Codex

#colours
RED = Fore.RED
BLUE = Fore.BLUE
YELLOW = Fore.YELLOW
CYAN = Fore.CYAN
L_GREEN = Fore.LIGHTGREEN_EX
GREEN = Fore.GREEN
WHITE = Fore.WHITE

#functions
functions = ["Basic Calculations","Matrix Calculations","Advanced Algebra","Calculus","Statistics and Probability","Vector Mathematics","Graphing Engine","Number Theory","Complex Mathematics","Linear Algebra - SUPER Advanced","Geometry","Differential Equations"]

def style():
    print(f"{YELLOW}CHOOSE THE FUNCTION IN WHICH YOU WANT TO OPERATE ON!")
    for i in range(len(functions)):
        str_fn = functions[i]
        num = f"{CYAN}[{i+1}]"
        print(num, end=" ")
        for j in range(len(str_fn)):
            if(i%2 == 0):
                print(f"{GREEN}", end="")
            else:
                print(f"{L_GREEN}", end="")
            print(str_fn[j], end="", flush=True)
            time.sleep(0.03)
        print(f"{WHITE}")
  
def Basic_Calculations():
    values = []
    print(references.basic_calculations)
    print("Calculate --> ", end="")
    calc = input()
    calc_str = str(calc)
    for i in range(len(calc_str)):
        if calc_str[i] in Codex:
            values.append(Codex[calc_str[i]])
    print(values)
    
    # if type(calc) == str:
    #     print(f"{RED}Invalid Input!")
    # else:
    #     try:
    #         cal = int(calc)

    
    print(f"{WHITE}")
def main():
    style()
    choice = int(input())
    if choice == 1:
        Basic_Calculations()
        
if __name__ == "__main__":
    main()