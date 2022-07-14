# Q.9 You have a dictionary called Shopping

# 1.I want to see the shopping list as the file view.
# 2.Then I will ask the user which item do you want to buy.
# 3.After that the username will be given then the user will 
#       be asked to input such as how many items do you want.
# 4.Then you have to remove that number of items from the file.
# 5.If you want to add shopping items then you have to insert in the same file.

import json
a={
    "shopping_list":
        { 
            "chaco":"15",
            "Biscuits":"50",
            "Diary_milk":"30",
            "ice_cream":"20",
        } 
}
with open("Q9.json","w") as f:
    json.dump(a,f,indent=2)
with open("Q9.json","r")as fp:
    b=json.load(fp)
    print(b)
    print(type(b))
    user=input("which item do u want:")
    user2=int(input("how many items do u want:"))
    for i in b:
        for j in b[i]:
            if user in b[i]:
                if j==user and int(b[i][j])>user2:
                    e=int(b[i][j])>user2
                    b[i][j]=str(e)
            elif j!=user:
                print("no")
                break
    item=input("enter the item")
    quntity=int(input("enter the number:"))
    b[i].update({item:quntity})
print(b)
