password = 1729

chances = 4

print("Enter Pin : ")
while chances >= 0:
    pin = int(input(" > "))
    if len(str(pin)) == 4:
        if pin == password:
            print("Correct Pin ....  ")
            print("thank you")
            break
        else:
            print("Incorrect Pin ....")
            print(f"{chances} Chances Remaining ..")
            chances -= 1
    else:
        print("Minimum 4 characters")
