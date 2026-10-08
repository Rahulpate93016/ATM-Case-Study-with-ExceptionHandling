from ATM_Excep_Exception import insufficient_Balance_Error
from ATM_Excep_Exception import DepositError
from ATM_Excep_Exception import WithdrawError
Balance=500  ## Global variable
def deposit():
    dep=float(input("Enter your deposit amount: "))
    if dep<=0:
        raise DepositError
    else:
        global Balance
        Balance=Balance+dep
        print("="*50)
        print("Your Account XXXXXXX123 Credit with INR:{}".format(dep))
        print(("Your Account XXXXXXX123 Balance is:{}".format(Balance)))
        print("Thank you Visit Again")
        print("=" * 50)
def withdraw():
    global Balance
    withdraw = float(input("Enter your withdraw amount: "))
    if  withdraw <= 0:
        raise WithdrawError
    elif withdraw>Balance:
        raise insufficient_Balance_Error
    else:

        Balance=Balance-withdraw
        print("=" * 50)
        print("Your Account XXXXXXX123 debit with INR:{}".format(withdraw))
        print(("Your Account XXXXXXX123 Balance is:{}".format(Balance)))
        print("Thank you Visit Again")
        print("=" * 50)

def balance_enquery():
    print("=" * 50)
    print("Your Account XXXXXXX123 Balance is INR:{}".format(Balance))
