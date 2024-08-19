dict={1:"Monday",2:"Tuesday",3:"Wednesday",4:"Thursday",5:"Friday",6:"Saturday",7:"Sunday"}
n= int(input("Enter A Digit Between 1&7:"))
if n in dict:
    print(dict.get(n))
else:
    print("Invalid Number")

