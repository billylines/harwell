name = []

inp = 0

while (inp != 3):
  
  inp = input("What do you want to do? (1 = add a name, 2 = print the names, 3 = quit, 4 = search for name) ")
  
  if (inp == 1):
    new_name = raw_input("Insert name: ")
    name.append(new_name)
  elif (inp == 2):
    for n in name:
      print n
  elif (inp == 4):
    search_name = raw_input("What name do you want to search? ")
    if search_name in name:
      print "The name has been found!"
    else:
      print "It's not there!"