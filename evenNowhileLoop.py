#while loop
#even number

n1= int(input("Enter the number: "))
end= int(input("Enter last number"))

while(n1<=end):
    if(n1%2==0):
        print(f"Even number: {n1}")
    n1+=1    
