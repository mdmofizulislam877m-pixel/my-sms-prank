import time

print("--- SMS Prank Tool Starting ---")
number = input("Enter Target Number: ")
amount = int(input("Enter Amount of SMS: "))

for i in range(amount):
    print(f"[{i+1}] Sending SMS to -> {number}")
    time.sleep(1)

print("Prank Completed Successfully!"
