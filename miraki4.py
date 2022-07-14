# Q4.Python dictionary(sort by key) Wrote a program to
#  convert an object to Data ::
import json
a={
    '4': 5, 
    '6': 7, 
    '1': 3, 
    '2': 4}
with open("myfile.json","w")as f:
    json.dump(a,f,indent=4)
    


# import json
# a={'4': 5, '6': 7, '1': 3, '2': 4}
# print(json.dumps(a,indent=4,sort_keys=True))