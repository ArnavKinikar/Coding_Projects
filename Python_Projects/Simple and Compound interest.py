prin = int(input("Enter the principle Amount: "))
rate = float(input("Enter Rate of Interest: "))
time = float(input("Enter the time period: "))

SI = prin * rate * time / 100

CI = prin * ((1 + rate / 100) ** time)

print("The Simple Interest is: " + str(SI))
print("The Compound Interest is: " + str(CI))