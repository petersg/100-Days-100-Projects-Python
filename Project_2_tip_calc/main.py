#
#   TIP CALCULATOR
#

print('Welcome to tip calculator')
total_bill = float(input('What was total bill? '))
total_ppl = float(input('How many people to split the bill: '))
percent = float(input('What percent you want to tip (10,12 or 15)? '))
total = total_bill/total_ppl%percent
print('Each one should pay: ', total)