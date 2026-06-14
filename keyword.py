def keyword(final):
    return(final)
bill=int(input(("amount to pay: $ ", 2.50)))
payed=int(input("Enter amount to pay:=$ "))
if payed>=bill:
    print(("The change is:$", payed-bill))
