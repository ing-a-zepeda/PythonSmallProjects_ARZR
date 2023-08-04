# link: https://instagram.com/p/CuemW5GvcRr

nip = 0

while True:
    # Login with NIP
    while True:
        if nip == 0:
        
            try:
                nip = int(input("Type your nip 4 numbers: "))

            except:
                print("Please type 4 numbers")
                nip = 0
                continue
            
            if nip < 10000 and nip > 999:
                if nip == 1234:
                    print("Welcome User\n")
                    break
                else:
                    nip = 0
                    print("NIP incorrect")
                    continue
            else:
                nip = 0
                print("Please type 4 numbers")
        elif nip == 1234:
            break

    balance = 10000
    print("     ATM")
    print("""
1)   Balance
2)   Withdraw
3)   Deposit
4)   Quit
          """)

    try:
        Option = int(input("Enter Option: "))
    except Exception as e:
        print("Error", e)
        print("Enter 1,2,3, or 4 only")
        continue

    if Option == 1:
        print("Balance $", balance)

    if Option == 2:
        while True:
            print("Balance $", balance)
            try:
                Withdraw = float(input("Enter Withdraw amount $"))
            except Exception as e:
                print("Error", e)
                print("Enter numbers only")
                continue

            if Withdraw > 0:
                forewardbalance = (balance-Withdraw)
                print("foreward Balance $", forewardbalance)
                break
            elif Withdraw>balance:
                print("No funs in account")
                break
            else:
                print("None withdraw mande")
                break
    
    if Option == 3:
        while True:
            print("Balance $", balance)
            try:
                Deposit = float(input("Enter deposit amount $"))
            except Exception as e:
                print("Error", e)
                print("Enter numbers only")
                continue

            if Deposit>0:
                forewardbalance = (balance + Deposit)
                print("Forewardbalance $", forewardbalance)
                break
            else:
                print("None deposit made")
                break

    if Option == 4:
        exit()