# ##convert json file to python
# import json
# a='{"a":1,"b":2,"c":3,"d":4,"e":5}'
# b=json.loads(a)
# print(type(b))
# print(b)

###convert python object to json
# import json
# a={"a":1,"b":2,"c":3,"d":4,"e":5}
# b=json.dumps(a)
# print(type(b))
# print(b)


# ##sort_keys()
# import json
# a={"a":1,"d":2,"e":3,"c":4,"h":5}
# print(json.dumps(a,indent=4,sort_keys=True))

# # ##create json file
# import json
# a={"a":1,"d":2,"e":3,"c":4,"h":5}
# with open("mydad.json","w")as f:
#     json.dump(a,f,indent=2)


###read json file
# import json
# with open("mydad.json","r")as f:
#     b=json.load(f)
# print(b)
