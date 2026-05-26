# Basic Star Pattern
print("Star Pattern \n")
for i in range(1,6):
  for j in range(i):
    print("*", end="")
  print('\n')

#Inverted Star Pattern
print("Inverted Star Pattern \n")
for i in range(6,1,-1):
  for j in range(i, 1, -1):
    print("*", end="")
  print('\n')

def no_notes(a):
  Q = [2000, 500, 200, 100, 50, 20, 10]
  x = 0
  for i in range(7):
    q = Q[i]
    x = a//q
    print("Notes of {} = {}".format(q, x))
    a = a%q

amount = int(input("Enter Total Amount"))
no_notes(amount) 


