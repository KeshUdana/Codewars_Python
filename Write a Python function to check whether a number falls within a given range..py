while True:
  n1=float(input("Enter 1st number of range: "))
  n2=float(input("Enter 2nd number of range: "))
  NUM=float(input("Enter number you want to find range of: "))
  
  #using user defined function
  def tst_rng(num):
    if n1< num<n2:
      return("In range")
    else:
      return("Not in range")

  print(tst_rng(NUM))
  #Checking if user wants to continue process
  choice=str(input("Do you still wish to continue?(press 'y' : ").lower())
  if choice=="q":
    break
