amount_due = 50
accepted_coins = [25, 10, 5]

while True:
    value = int(input("Insert coin: "))
    if value in accepted_coins:
        amount_due -= value

        if amount_due <= 0:
            amount_due *= -1
            print("Change Owed:", amount_due)
            break

    print("Amount Due:", amount_due)
