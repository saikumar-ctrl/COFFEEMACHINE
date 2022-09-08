MENU={
     "tea":{
    "ingrediants" :  {
        "water":50,
        "coffee":10,
    },
    'cost':20
     },
     "buttermilk":{
         "ingrediants":{
             "water":100,
             "milk":150,
             "coffee":20
         },
         'cost':40
     },
    "chacobar":{
        "ingrediants":{
           "water":200,
            "milk":100,
           "coffee":30
        },
        "cost":50
    }

}
resources={
    "water":500,
    "milk":400,
    "coffee":200
}
def is_avaible(ingrediants):
    for i in ingrediants['ingrediants']:
        if ingrediants['ingrediants'][i] >=resources[i]:
            print(f'sorry not enough {i}')
            return False
    return True

profit=0
is_on=True
while is_on:
        choice=input('what would you like? :(tea/buttermilk/chacobar): ')
        if choice=="off":
            is_on=False
        elif choice=="report":
            print(f'water: {resources["water"]}ml')
            print(f'milk: {resources["milk"]}ml')
            print(f'coffee:{resources["coffee"]}g')
            print(f'money:{profit}$')
        else:
            ing=MENU[choice]
            if is_avaible(ing):
                for i in ing['ingrediants']:
                    resources[i]-=ing['ingrediants'][i]
                Money=int(input('Insert money you have for dring: '))
                if Money>ing["cost"]:
                   profit+=ing['cost']
                   print(f'your drink{choice} is redy enjoy......')
                   print(f"The cost is {ing['cost']} your change remaing is {Money-ing['cost']} refunde")
                else:
                    print("You have no enough moeny to get drink")




