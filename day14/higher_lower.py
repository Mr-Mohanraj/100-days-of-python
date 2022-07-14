data = [
{
'name':'instagram',
'follower_count':346,
'description': 'Social media platfrom',
'country': 'United States'
},
{
'name':'Cristiano Ronaldo',
'follower_count':215,
'description': 'Foodboller',
'country': 'Portugal'
},
{
'name':'Dwayne Johnson',
'follower_count': 181,
'description':'Actor and Professional Wrestler',
'country':'United States'
}
]



import random
def format_print(account):
    account_name = account['name']
    account_desc = account['description']
    #account_followers = account['follower_count']
    account_country = account['country']
    return f"{account_name}, {account_desc}, from {account_country}"

score = 0
should_run = True

while should_run:
    
    account_a = random.choice(data)
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)


    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']
    
    
    print(f"Compare A: {format_print(account_a)}")

    print("VS")

    print(f"Compare B:  {format_print(account_b)}")
    
    user_guess = input("Who has most followers?. Type 'A' or 'B' : ").lower()
    
    print(" ")
    
    if user_guess == 'a':
        if a_follower_count > b_follower_count:
            score += 1
        else:
            should_run = False
    elif user_guess == 'b':
        if a_follower_count < b_follower_count:
            score += 1
        else:
            should_run = False
    else:
        print("Please enter A OR B ")

print(f"Your Score: {score}")