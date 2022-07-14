
# Q8.You have the details of four employers in the list:-
# o/p:{ 
#      "emp1":{ "name":"nilam",
#        "Designation":"programmer",
#        "Age":"34",
#        "salary":"24000",
#          }

#     "emp2":
#       { "name":"komal",
#         "Designation":"Trainee",
#         "Age":"24",
#         "salary":"20000" ,
#         }

 
#     "emp3":
#        { "name":"anuradha",
#          "Designation":"HR",
#          "Age":"25",
#          "salary":"40000",
#          }


#     "emp4":
#        { "name":"Abhishek",
#          "Designation":"Manager",
#          "Age":"29",
#        }
#  }


# 1.Now you have to create 4 dictionaries like amp1 amp2 amp3 and amp4.
# 2.Every employee should have name, designation, forward and salary 
#                                                in the dictionary.
# 3.And all this is the dictionary key in which I have given the value
#                                                        in the list.
# 4.You have to create a json file using this? Like given below.
import json
a=["neelam","programer","24","2400",]
b=["komal","trainer","24","20000"]
c=["anuradha","R","25","40000"]
d=["Abhishek","manager","29","63000"]
key=["name","disignation","age","salary"]
emp1={}
emp2={}
emp3={}
emp4={}
dic={}
for i in range(len(a)):
    emp1.update({key[i]:a[i]})
for j in range(len(b)):
    emp2.update({key[j]:b[j]})
for k in range(len(c)):
    emp3.update({key[k]:c[k]})
for n in range(len(d)):
    emp4.update({key[n]:d[n]})
dic={"emp1":emp1,"emp2":emp2,"emp3":emp3,"emp4":emp4}
with open("Q8.json","w")as f:
    json.dump(dic,f,indent=4)
