print("Files app")
while quit == False:
  option = input("files>>> ")
  if option == "open":
    print("Input file name.")
    option = input("files/open>>> ")
    if option in files:
      file = option
      print(f"FILE: {file}")
      option = input(f"files/open/{file}>>> ")
      if option == "read":
        #print( FILE DATA GOES HERE )
