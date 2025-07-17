#check if an input string is an palindrome
#palindrome checker 
def palindrome_checker():
   pal_choice = input("enter your palindrome in capital letters: ")
   pal_choice = pal_choice.upper()
   pal2_choice = pal_choice[::-1]

   if pal_choice == pal2_choice:
      print(f"it is a palindrome: {pal_choice} equals {pal2_choice}!!!")
   else:
      print("thats not a palindrome!!!")
# taking user input 
def greet():
 name = input("enter your name : ")
 print(f"hello, {name} welcome to palindrome checker!")
 choice = input("do you want to use the palindrome checker? (yes/no): ")
 if choice.lower() ==  "yes":
     palindrome_checker()
 else:
     print("Alright, Byee!!")
greet()

