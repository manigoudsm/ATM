from ATMMenu import menu
from ATMoperations import deposit,withdraw,balenq
from ATMExcept import DepositError,InsufFundError,ATMError,WithdrawError
while(True):
    menu()
    try:
        ch=int(input("Enter ur choice"))
        match(ch):
            case 1:
                try:
                    deposit()
                except ValueError:\
                    print("Dont try to withdraw alnums ")
                except DepositError:
                    print("Dont try to Deposit -ve ")
            case 2:
                try:
                    withdraw()
                except ValueError:
                    print("Dont try to withdraw  alnums,str,sym")
                except WithdrawError:
                    print("Dont try to withdraw  -ve amt")
                except InsufFundError:
                    print("ur act doesnt have money")
                except ATMError:
                    print("Unable to print")
            case 3:
                balenq()
            case 4:
                print("Thx")
            case _:
                print("wrong input")
    except ValueError:
        print("dont")