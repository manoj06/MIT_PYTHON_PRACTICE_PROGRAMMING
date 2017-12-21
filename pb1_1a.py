annual_salary=float(raw_input("Enter annual salary:"));
portion_saved=float(raw_input("Enter the portion saved:"));
total_cost=float(raw_input("Enter total cost:"));


portion_down_payment=0.25

down_payment=portion_down_payment*total_cost

current_savings=0.0

r=0.04

monthly_salary=annual_salary/12.0

i=0;

while(current_savings<down_payment):
    current_savings+=current_savings*r/12
    current_savings+=monthly_salary*portion_saved
    i+=1
print(i);
