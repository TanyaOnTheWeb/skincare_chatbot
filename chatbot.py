import pandas as pd

#Loading dataset
data = pd.read_csv("ingredients.csv")

print('Welcome to Skincare Ingredient Bot')

#Ask user questions
skin_type = input('Enter your skin type: ')
problem = input('Enter your skin problem: ')


#Find matching row 
row = data[data['Problem'].str.lower() == problem.lower()]

if row.empty:
    print("Sorry,I don't have data for this problem yet")
else:
    print("\n Good ingredeints: ")

    for col in ["Good_1","Good_2","Good_3","Good_4"]:
        value = row[col].values[0]
        if str(value) != "nan":
            print("-",value)

    print("\n Avoid ingredients:")
    
    for col in ["Avoid_1","Avoid_2","Avoid_3","Avoid_4"]:
        value = row[col].values[0]
        if str(value) != "nan":
            print("-",value)

print("\n🧾 Skincare history")

used_before = input("Have you used skincare products before? (yes/no): ")

if used_before.lower() == "yes":
    product = input("Which product did you use? ")
    reaction = input("Did you face any reaction? (yes/no): ")

    if reaction.lower() == "yes":
        print("⚠ Noted! I will avoid harsh ingredients for you.")
    else:
        print("✅ Great! That product worked fine for you.")

else:
    print("👍 No previous products used.")

print("\n Thanks for using the bot!")