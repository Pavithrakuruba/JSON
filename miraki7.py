# Q7.Can convert text file data to file data as given below?

# a={Name ,Abhishek, Designation ,CEO of navgurukul,Gender, male,Age, 29}
# o/p
# {
#     “Name”: “Abhishek”,
#     “Designation”: “CEO of      navgurukul”,
#     “Gender”:”male”,
#     “Age”: “29”
#     }


# import json
# a={"Name","pavi","gender","female"}
#     print(json.dump(),a,indent=4,separators=(",",":"))

import json
a=["Name" ,"Abhishek", "Designation" ,"CEO of navgurukul,Gender", "male",
"Age", "29"]
key=[]
value=[]
for i in range(len(a)):
    if i%2==0:
        key.append(a[i])
    else:
        value.append(a[i])
c=dict(zip(key,value))
s=open("mystring.json","w")
a=json.dump(c,s)



