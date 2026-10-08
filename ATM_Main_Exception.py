from ATM_Menu_Exception import Menu
from ATM_Operations_Exception import deposit, withdraw, balance_enquery
from ATM_Excep_Exception import insufficient_Balance_Error, DepositError, WithdrawError


while(True):
    Menu()

    ch = int(input("Enter Your Choose:"))
    match(ch):
        case 1:
            try:
                deposit()
            except ValueError:
                print("Dont Enter str,Special Charecter..:")
            except DepositError:
                print("Don't try.. Zero for Deposit..")
        case 2:
            try:
                withdraw()
            except ValueError:
                print("Dont Enter str,Special Charecter..:")
            except WithdrawError:
                print("Don't try.. Zero for Withdraw")
            except insufficient_Balance_Error:
                print("Your Balance is Insufficient..")
        case 3 :
                balance_enquery()
        case 4:
            print("...Thank you for using our application...!")
            break
        case default:
            print("Wrong Choice...try again!")


