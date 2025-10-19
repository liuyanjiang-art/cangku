
rivers = {
  "London": "Thames", 
  "Leeds": "Aire", 
  "Liverpool": "Mersey",
  "York": "Ouse"
}

# loop through the dict extracting key and value

for c,r in rivers.items():
    print( c,r )
for i in rivers.keys():
  print(i)
for i in rivers.values():
  print(i)
  
    
# create 2 further for loops to iterate: 1. just through the keys, 2. just through the values
# hint: we looked at built in function for dicts last session