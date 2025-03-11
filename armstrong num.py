a=int(input ("ENTER A VALUE TO CONVERT: "))
sum=0
temp =a
while temp>0:
    digit=temp%10
    temp//=10
    sum=sum+(digit**3)
if sum == a:
    print("THE GIVEN NUMBER IS ARMSTRONG")
else:
    print("THE GIVEN NUMBER IS NOT ARMSTRONG")   

