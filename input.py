
import math


def main() :
    x = input ("please enter the number of bottles you have that are 1L or less\n")
    x = int (x)

    a = float (x * 0.10)
    
    
    

    y = input ("How many bottles do you have that are more than 1L?\n")

    y = int (y)

    b =  float (y *0.25)
    
    


    z = a+b
    z ="{:.2f}".format(z)
    

    print (" Your refund is " + "$"+  str(z))





if __name__ == "__main__":
    
    main()