"""
Looping & Control Flow
"""
#for 
"""
colors=["Red", "Green", "Blue"]
for color in colors:
    print(color)
  
Red
Green
Blue
"""
#using range; also range has step ex: for num in range(1,5,2) starting from 1 with step 2 
"""
for num in range(5):
   print(num)
  
0
1
2
3
4
"""
#if & elif & else
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#while 
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
