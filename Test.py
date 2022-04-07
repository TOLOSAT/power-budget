import json

obdh = {"test" : 8, "safe" :  4, "overload" : 10}
thermal = {"test" : 2, "safe" : 2, "truc" : 7}
mode = {"test" : {"obdh" : "test" , "thermal" : "test"}, "safe" : {"obdh" : "safe", "thermal" : "safe"}}

file = {"mode" : mode, "sous-sys" :  { "obdh" : obdh, "thermal" :  thermal}}

st = json.JSONEncoder().encode(file)
print(st)

with open("data.json", "r+") as fichier :
    fichier.write(st)