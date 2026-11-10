age = int(input('What is your age--> '))
is_employed = bool(input("Are you employed? (true/false) --> "))
credit_score = int(input('What is your credit score--> '))
annual_income = float(input('What is your annual income--> '))
has_collateral = bool(input('Do you have collateral? (true/false) --> '))

base_rate=0.0
if age >= 21 and is_employed == True:
    print('your are eligible')
#tier_1
if credit_score >= 750:
    print('you have a high credit score')
    if annual_income >= 100000:
        base_rate=4.5
        print('you base rate is', base_rate)
    else:
        base_rate=5.0
        print('your base interest ', base_rate)
#tier2
elif credit_score >= 600:
    print('you have a fair credit score')
    if has_collateral:
        base_rate= 7.0
        print('your base rate is', base_rate)
    elif annual_income < 40000:
        base_rate= 9.5
        print('your base rate is', base_rate)
    else:
        base_rate= 8.0
        print('your base rate is', base_rate)
else:
    print('rejected, your credit score is too low')
