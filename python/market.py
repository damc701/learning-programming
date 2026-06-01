client_ident =[]
client_fullname=[]
client_adress=[]
client_mobile=[]
client_email=[]
client_gender=[]
client_age=[]


product_code=[]
product_name=[]
product_quantity=[]
product_unit_val=[]


def mainmenu():
 print(":::market main menu:::")
 print(
    "[1]. register client \n"\
    "[2]. register product \n"\
    "[3]. list client \n"\
    "[4]. list products \n"\
    "[5]. search client by ident \n"\
    "[6]. search product by code \n"\
    "[7]. update client  \n"\
    "[8]. update product \n"\
    "[9]. delete client \n"\
    "[10]. delete product \n"\
    "[11]. exit \n"
    ".::press any option::.")
 

# Main
menu_status = True
while menu_status:
    mainMenu()
    opt = int(input())
    
    if opt == 1:
        os.system('clear')
        print('...............................')
        print('........NEW CLIENTS............')
        print('...............................')

        ident = input('Client identification: ')
        client_ident.append(ident)
        fullname = input('Client fullname: ')
        client_fullname.append(fullname)
        print('Client has been registered successfully !!!')
        key = input('Press any option to back main menu.')
    elif opt == 3:
        os.system('clear')
        print('...............................')
        print('........LIST CLIENTS............')
        print('...............................')

        print('\n')
        print('-' * 50)
        print(f"{'Identification':<20} {'Fullname':<20}")
        print('-' * 50)
        i = 0
        while i < len(client_fullname):

            print(f'{client_ident[i]:<20} {client_fullname[i]:<20}')
            i+=1 
        
        key = input('\nPress any option to back main menu.')
    if opt == 11:
        print('Bye, bye')
        break
    if opt < 1 or opt > 11:
        key = input('Invalid option. Try again. \n' \
        'Press any key to continue.')
