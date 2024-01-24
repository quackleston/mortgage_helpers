# MORTGAGE HUMANITARIANS: menu based. create, view, amend, and delete products and quotes! :)

# PRODUCTS LIST
products = [["Home Loan Flexi", 2.3],["Santander Fresh Home Loan",
1.8],["Barclays First-Time Mortgage",1.98],["Le Chonker", 2.1]]

quotes = []


# ENTER TO CONTINUE(with easter egg!)
def enterC():
    enterCont = ":)"
    while enterCont != "":
        enterCont = input("\nPRESS ENTER TO CONTINUE\n")
    menu()


# TITLE
print("M O R T G A G E   H E L P E R S\n")


# CREATE PRODUCTS
def createProduct():
    print("\nCREATE NEW PRODUCT:")
    productName = input("please type in product name\n> ")
    productInterest = float(input("\nplease type in the interest rate\n> "))

    print("\nPRODUCT SUMMARY:")
    print(f"product name: {productName}\ninterest rate: {productInterest}")
    confirmation = input('''to proceed, type 1 to confirm product's details
press any key to quit
> ''')
    if confirmation == "1":
        products.append([productName, productInterest])
        print(f'''\nCREATING NEW PRODUCT
GENERATING PRODUCT...
new product name: {productName}
new product rate: {productInterest}''')
        enterC()
    else:
        createProduct()


# CREATE QUOTES
def createQuotes():
    print("\nCREATE NEW QUOTE:")
    quotesName = input("please enter customer name\n> ")
    loanAmount = float(input("\nplease input loan amount\n> "))
    loanTerm = float(input("\nplease input term of loan in year\n> "))*12

    print("\nLIST OF PRODUCTS:")
    for i in range(len(products)):
        print(f"{i + 1}. name: {products[i][0]} | interest rate: {products[i][1]}")
    productNum = int(input("\nselect a product number\n> "))-1
    while productNum not in range(len(products)+1):
        productNUm = int(input("invalid input! select a product number\n> ")) - 1

    interestRate = float((products[productNum][1])/100)/12
    monthAmount = loanAmount * ((interestRate * ((1 + interestRate) **
                                                loanTerm)) / ((1 + interestRate) ** loanTerm - 1))
    totalRepay = monthAmount * loanTerm

    monthAmount = round(monthAmount,2)
    totalRepay = round(totalRepay,2)

    print("\nPRODUCTS SUMMARY:")
    print(f"home loan product name: {products[productNum][0]} \nhome loan rate: {products[productNum][1]}\nmonthly repayment: {monthAmount}\ntotal repayment: {totalRepay}")
    quotes.append([quotesName, loanAmount, loanTerm, products[productNum][0], products[productNum][1], monthAmount, totalRepay])
    enterC()


# VIEW PRODUCTS
def viewProducts():
    print("\nLIST OF PRODUCTS:")
    for i in range(len(products)):
        print(f"{i + 1}. name: {products[i][0]} | interest rate: {products[i][1]}")
    enterC()

# VIEW QUOTES
def viewQuotes():
    print("\nLIST OF QUOTES:")
    for i in range(len(quotes)):
        print(f"{i + 1}. \ncustomer name: {quotes[i][0]}\nloan amount: {quotes[i][1]}\nloan term: {quotes[i][2]}\nloan product name: {quotes[i][3]}\nloan product rate: {quotes[i][4]}\nmonthly repayment: {quotes[i][5]}\ntotal repayment: {quotes[i][6]}")
    enterC()

# AMEND PRODUCTS
def amendProducts():
    print("AMEND PRODUCTS:\n")
    print("\nLIST OF PRODUCTS:")
    for i in range(len(products)):
        print(f"{i + 1}. name: {products[i][0]} | interest rate: {products[i][1]}")
    amendPro = int(input("select a product to amend\n> ")) - 1
    while amendPro not in range(len(products)):
        amendPro = int(input("invalid input! select a product to amend\n> ")) - 1

    print(f"product name: {products[amendPro][0]}")
    newName = input("new product name (q/Q to skip): ")
    if newName != "q" and newName != "Q":
        products[amendPro][0] = newName
    print(f"interest rate: {products[amendPro][1]}")
    newRate = input("new product name (q/Q to skip): ")
    if newRate != "q" and newRate != "Q":
        products[amendPro][1] = float(newRate)
    print("\nPRODUCTS SUMMARY:")
    print(f"name: {products[amendPro][0]} \ninterest rate: {products[amendPro][1]}")
    enterC()


# AMEND QUOTES
def amendQuotes():
    print("\nLIST OF QUOTES:")
    for i in range(len(quotes)):
        print(
            f"{i + 1}. \ncustomer name: {quotes[i][0]}\nloan amount: {quotes[i][1]}\nloan term: {quotes[i][2]}\nloan product name: {quotes[i][3]}\nloan product rate: {quotes[i][4]}\nmonthly repayment: {quotes[i][5]}\ntotal repayment: {quotes[i][6]}")

    amendQuo = input("\nselect a quote to amend (q/Q to exit)\n> ")

    validAns = False

    while validAns == False:
        if amendQuo.isnumeric():
            if int(amendQuo) - 1 not in range(len(quotes)):
                validAns = False
                amendQuo = input("\ninvalid input! select a quote to amend (q/Q to exit)\n> ")
            else:
                validAns = True
        elif amendQuo.isalpha() or amendQuo.isspace():
            if amendQuo == "q" or amendQuo == "Q":
                validAns = True
                quotesMenu()
            else:
                validAns = False
                amendQuo = input("\ninvalid input! select a quote to amend (q/Q to exit)\n> ")

    amendQuo = int(amendQuo)-1
    print(f"\ncustomer name: {quotes[amendQuo][0]}")
    nameNew = input("new customer name (q/Q to skip): ")
    if nameNew != "q" and nameNew != "Q":
        quotes[amendQuo][0] = nameNew
    print(f"\nloan amount: {quotes[amendQuo][1]}")
    newLoan = float(input("new loan amount (q/Q to skip): "))
    if newLoan != "q" and newLoan != "Q":
        quotes[amendQuo][1] = float(newLoan)
    print(f"\nloan term: {quotes[amendQuo][2]}")
    loanTerm = int(input("new loan amount (q/Q to skip): "))
    if loanTerm != "q" and loanTerm != "Q":
        quotes[amendQuo][2] = float(loanTerm)

    print(f"\nloan product name: {quotes[amendQuo][3]}")

    print("\nLIST OF PRODUCTS:")
    for i in range(len(products)):
        print(f"{i + 1}. name: {products[i][0]} | interest rate: {products[i][1]}")

    loanName = int(input("\nselect the number from above for the new loan product (q/Q to skip): ")) - 1
    if loanName != "q" and loanName != "Q":
        quotes[amendQuo][3] = products[loanName][0]
        quotes[amendQuo][4] = products[loanName][1]

    print(f"\nmonthly payment: {quotes[amendQuo][5]}")
    monthlyPay = int(input("new monthly payment (q/Q to skip): "))
    if monthlyPay != "q" and monthlyPay != "Q":
        quotes[amendQuo][5] = float(monthlyPay)
    print(f"\ntotal payment: {quotes[amendQuo][6]}")
    totalPay = int(input("new total payment (q/Q to skip): "))
    if totalPay != "q" and totalPay != "Q":
        quotes[amendQuo][6] = float(totalPay)

    print("\nQUOTES SUMMARY:")
    print( f"customer name: {quotes[amendQuotes()][0]}\nloan amount: {quotes[amendQuotes()][1]}\nloan term: {quotes[amendQuotes()][2]}\nloan product name: {quotes[amendQuotes()][3]}\nloan product rate: {quotes[amendQuotes()][4]}\nmonthly repayment: {quotes[amendQuotes()][5]}\ntotal repayment: {quotes[amendQuotes()][6]}")
    enterC()

# DELETE PRODUCTS
def deleteProducts():
    print("\nDELETE PRODUCTS:\n")
    print("LIST OF PRODUCTS:")
    for i in range(len(products)):
        print(f"{i + 1}. name: {products[i][0]} | interest rate: {products[i][1]}")
    deletePro = input("\nselect a product to delete (q/Q to exit)\n> ")

    validAnswer = False

    while validAnswer == False:
        if deletePro.isnumeric():
            if int(deletePro) - 1 not in range(len(products)):
                validAnswer = False
                deletePro = input("\ninvalid input! select a product to delete (q/Q to exit)\n> ")
            else:
                validAnswer = True
        elif deletePro.isalpha() or deletePro.isspace():
            if deletePro == "q" or deletePro == "Q":
                validAnswer = True
                productsMenu()
            else:
                validAnswer = False
                deletePro = input("\ninvalid input! select a product to delete (q/Q to exit)\n> ")

    # int(deletePro) - 1
    print("\ndelete:")
    print(f"name: {products[int(deletePro) - 1][0]} \ninterest rate: {products[int(deletePro) - 1][1]}")
    deleteConfirm = input("to confirm, type c/C (type enter to exit)\n> ")
    if deleteConfirm == "c" or deleteConfirm == "C":
        del products[int(deletePro) - 1]
        print("\ndeleted!")
        enterC()
    else:
        enterC()


# PRODUCTS MENU
def productsMenu():
    validAnswer = False
    iList = ["i", "ii", "iii", "iv", "v"]
    print("\nMORTGAGE PRODUCTS:")
    print("i. add product")
    print("ii. view products")
    print("iii. amend product")
    print("iv. delete product")
    print("v. return to main menu")
    while validAnswer == False:
        selection1 = input("\nplease select an option\n> ")
        if selection1.isnumeric():
            if int(selection1) <= 5 and int(selection1) >= 1:
                validAnswer = True
        else:
            if selection1 in iList:
                validAnswer = True
    if selection1 == "i" or selection1 == "1":
        createProduct()
    elif selection1 == "ii" or selection1 == "2":
        viewProducts()
    elif selection1 == "iii" or selection1 == "3":
        amendProducts()
    elif selection1 == "iv" or selection1 == "4":
        deleteProducts()
    else:
        print("")
        menu()

# QUOTES MENU
def quotesMenu():
    validAnswer = False
    iList2 = ["i", "ii", "iii", "iv"]
    print("\nMORTGAGE QUOTES:")
    print("i. create quotes")
    print("ii. view quotes")
    print("iii. amend quotes")
    print("iv. return to main menu")
    while validAnswer == False:
        selection1 = input("\nplease select an option\n> ")
        if selection1.isnumeric():
            if int(selection1) <= 4 and int(selection1) >= 1:
                validAnswer = True
        else:
            if selection1 in iList2:
                validAnswer = True
    if selection1 == "i" or selection1 == "1":
        createQuotes()
    elif selection1 == "ii" or selection1 == "2":
        viewQuotes()
    elif selection1 == "iii" or selection1 == "3":
        amendQuotes()
    elif selection1 == "iv" or selection1 == "4":
        print("")
        menu()

# MAIN MENU
def menu():
    validAnswer = False
    print("MENU:\ni. manage products\nii. manage quotes\niii. quit")
    while validAnswer == False:
        selection1 = input("\nplease select an option\n> ")
        if selection1.isnumeric():
            if int(selection1) <= 3 and int(selection1) >= 1:
                validAnswer = True
        else:
            if selection1 == "i" or selection1 == "ii" or selection1 == "iii":
                validAnswer = True
    if selection1 == "i" or selection1 == "1":
        productsMenu()
    elif selection1 == "ii" or selection1 == "2":
        quotesMenu()
    elif selection1 == "iii" or selection1 == "3":
        print("THANK YOU FOR USING MORTGAGE HELPERS :)")
        quit()


menu()

