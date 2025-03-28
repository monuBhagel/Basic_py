myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}


# accessing nested dict

child1_name= myfamily["child1"]["name"]

print(child1_name)



# looping through nested dict

for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])