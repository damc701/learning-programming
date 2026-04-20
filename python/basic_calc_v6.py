import os

#function main memu
def main_menu():
    print("### MAIN MENU ###")
    print("[1], Addition")
    print("[2], Sustraccion")
    print("[3], Multiplication")
    print("[4], DIvicion")
    print("[5], Average")
    print("[6], All operarions")

os.system('clear')
#inputs
n1 = float(input("enter first number: "))
n2 = float(input("enter second number: "))
main_menu()
opt = int(input("enter any option: "))

match opt:
    case 1:
        add = n1 + n2 
        print(f"addition is: {add}")
    case 2:
        subs = n1 - n2 
        print(f"sustraccion is: {subs}")
    case 3:
        mult = n1 * n2 
        print(f"multiplication is: {mult}")
    case 4:
        div = n1 / n2 
        print(f"divition is: {div}")
    case 5:
        avg = (n1 + n2) / 2 
        print(f"average is: {avg}")
    case 6:
        add = n1 + n2 
        subs = n1 - n2
        mult = n1 * n2
        div = n1 / n2 
        avg = (n1 + n2) / 2
        print(f"addition is: {add}")
        print(f"sustraciion is: {subs}")
        print(f"multiplication is: {mult}")
        print(f"divition is: {div}")
        print(f"average is: {avg}")