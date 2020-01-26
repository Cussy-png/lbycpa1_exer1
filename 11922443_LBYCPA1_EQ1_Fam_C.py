def start():
   while True:
      print(" ****Welcome to our automated milktea ordering system**** ")
      print("")
      print(" For today's milk tea, we offer ")
      print("")

      print( " Type 1 for Original Milk Tea " )
      print( " Type 2 for Pearl Milk Tea " )
      print( " Type 3 for Coffee Milk Tea " )
      print( " Type q to quit " )

      choice = input(" Select your Milk Tea of choice: ")

      if choice =='1': 
         print(" Original Milk Tea will cost PHP60, Thank you! ") 
      elif choice == '2': 
         print(" Pearl Milk Tea will cost PHP65, Thank you! ")
      elif choice == '3':
         print( " Coffee Jelly Milk Tea will cost 70,Thank you!" )
      elif choice == 'q': 
         print(" Thank you for Ordering!" )
         exit
         
start()

