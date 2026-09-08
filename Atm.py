import math
total_balance=100000
withdrawl_ammount=int(input("Enter how many Ruppes you want to withdraw : "))
if withdrawl_ammount%500==0:
    current_bal=total_balance-withdrawl_ammount
    print(f"You have withdrawled {withdrawl_ammount} Rs and your new balance is {current_bal}")
else:
    adjusted_balance=math.floor(withdrawl_ammount/500)*500
    print("Your adjusted ammount is : ",adjusted_balance)
    current_bal=total_balance-adjusted_balance
    print(f"Your withdrawn ammount is {adjusted_balance} and your new balance is {current_bal} ")