# Dictionary is a collection of key value pairs
# Properties:
# -> immutable
# -> unordered
# -> indexed
# -> cannot contain duplicate keys

a={
    "name":"yathin",
    "place":"hyd",
    "marks":[98,99,100],
    "b":{"language":"python",      # nested dictionaries
        "gender":"male"}
}

print(a)
print(a["name"])
print(a["place"])
print(a["marks"])
print(a["b"]["language"])
a["marks"]=[96,97,98]
print(a["marks"])

# Dictionary methods
print(list(a.keys()))    #prints the keys of dictionary
print(a.values())        #prints the values of dictionary
print(a.items())         #prints (key,value)tuples for all contents of dictionary
update_a={
    "clg":"IIITNR"
}
a.update(update_a)      #updates dictionary by adding key, value of update_a
print(a)

print(a.get("name"))
