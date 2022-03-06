income = int(input('please inter number of income;'))

if income <1000 :
    taxation = income
if 1000<=income<=2500 :
    taxation = income-((income*10)//100)
if 2500<income<=4000 :
    taxation = income-((income*15)//100)
if 4000<income<=6000 :
    taxation = income-((income*20)//100)
if income>8000 :
    taxation = income-((income*30)//100)
print(taxation)
