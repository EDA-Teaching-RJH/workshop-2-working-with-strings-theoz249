def main():
    slow = input("user say something .")
    print(myFunction(slow))

def myFunction(text):
  #Your code goes here.
  x = text.replace(" ",".")
  return x
main()
