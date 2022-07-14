# Q.6 Python objects write programs because of their unique value?
import json
a='{"a":  1,"a":  2,"a":  3, "a": 4,   "b": 1, "b": 2}'
f=open("myfile","w")
json.dump(a,f,indent=6)
# f.close()




# a={
#     "a":  1, 
#     "a":  2, 
#     "a":  3, 
#     "a": 4, 
#     "b": 1, 
#     "b": 2
# }
###o/p{'a': 4, 'b': 2}