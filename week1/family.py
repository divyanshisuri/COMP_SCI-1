Family = []
# List with dictionary records placed in a list
Family.append({
               "Dad": "Amit",  
               "Mom": "Karuna",  
               "Children": ["Lakshay","Deven","Divyanshi "],
               "Last Name": "Suri" , 
               "Residence": "San Diego",
               "Population":"4" 
              })
Family.append({
              "Pets": "None",  
              "Near_Parks": "Heritage Park",  
              "DOBs": ["February 21", "April 18", "October 9 ", "October 26"],
              "Cousins": ["Simran","Angel", "Aanya"],  
              "Emails":["divyanshi.suri@gmail.com", "X", "X"]  
              })

print (Family)


a = input("Enter key: " )
b = input("Enter value: " )

def for_loop(key, value):
  for data in Family:
    if(data[key]) == value:
      print(data[key])
      return
for_loop(a,b)

def while_loop(key, value):
  i = 0
  while i < len(Family):
    if (Family[i][key] == value):
      print(Family[i][key])
      return
    i +=1
while_loop(a,b)

def recursive_loop(i, key, value):
  if (i < len(Family)):
    if (Family[i][key] == value):
      print(Family[i][key])
      return
    i += 1
    recursive_loop(i, key, value)
  return
recursive_loop(0,a,b)

def driver():
  
