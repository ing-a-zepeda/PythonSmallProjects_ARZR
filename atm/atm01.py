# link: https://instagram.com/p/CuemW5GvcRr

while True:
    balance = 10000
    print("  ATM  ")
    print("""
1)   Balance
2)   Withdraw
3)   Deposit
4)   Quit
          """)

    try:
        Option = int(input("Enter Option: "))
    except:
        print("Error", e)
        print("Enter 1,2,3, or 4 only")
        continue

    if Option == 1:
        print("Balance $", balance)

    if Option == 2:
        print("Balance $", balance)
        Withdraw = float(input("Enter Withdraw amount $"))
        if Withdraw > 0:
            forewardbalance = (balance-Withdraw)
            print("foreward Balance $", forewardbalance)
        elif Withdraw>balance:
            print("No funs in account")
        else:
            print("None withdraw mande")
    
    if Option == 3:
        print("Balance $", balance)
        Deposit = float(input("Enter deposit amount $"))
        if Deposit>0:
            forewardbalance = (balance + Deposit)
            print("Forewardbalance $", forewardbalance)
        else:
            print("None deposit made")

    if Option == 4:
        exit()