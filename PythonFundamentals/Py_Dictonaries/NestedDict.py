###A dictonaries can contain dictonaries is called nested dictonaries.

##create a nested dictonaries

nestedDictonaries={
    "emp1":{ "name":"Bibhu",
            "Number":1234567890,
            "location":"Bangalore"
            },
            "emp2":{ "name":"Richa",
                    "Number":987654321,
                    "location":"Bettiah"
                    },
                    "emp3":{"name":"Jayant",
                            "Number":2345678987,
                            "location":"Narkatiaganj"
                            }
}

print(nestedDictonaries)

##If you want to add three dictonaries into one dictonaries
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}
myFamily={"child1":child1,
          "child2":child2,
          "child3":child3
          }
print(myFamily)

#Access Items in Nested Dictionaries
print(myFamily["child1"]["name"])

#Loop Through Nested Dictionaries
##we can loop through nested dictonaries using items() methods

for x,obj in myFamily.items():
    print(x)
    for y in obj:
        print(obj[y])