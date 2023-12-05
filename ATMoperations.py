from ATMExcept import DepositError,InsufFundError,ATMError,WithdrawError
bal=500.00   #Here bal is global variable
atmamt=0
def deposit():
    damt=float(input("Enter or Deposit Amt"))#value Error
    if(damt<=0):
        raise DepositError
    else:
        global bal,atmamt
        bal=bal+damt
        atmamt=atmamt+damt
        print("Ur acctxxxxx123 credited with INR:{}".format(damt))
        print("Now or Act Bal:{}".format(bal))
def withdraw():
    global bal,atmamt
    wamt=float(input("Enter ur withdraw amt:"))
    if (wamt<=0):
        raise WithdrawError
    elif((wamt+100)>bal):
        raise InsufFundError
    elif(atmamt<wamt):
        raise ATMError
    else:
        bal=bal-wamt
        atmamt=atmamt-wamt
        print("Ur Act xxxx Debited with INR:{}".format(wamt))
        print("Act Bal:{}".format(bal))
def balenq():
    print("act bal:{}".format(bal))

