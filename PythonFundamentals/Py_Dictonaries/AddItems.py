# Add Items in dictonaries can be done by referring a keyname of dictonaries

fruitDict={"name":"apple",
           "price":200
           }
print(fruitDict)
#Adding items

fruitDict["color"]="Red"
fruitDict["taste"]="Sweet"
print(fruitDict)

##Update dictonaries
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})
print(thisdict)