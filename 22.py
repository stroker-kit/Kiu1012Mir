import sys
p=0
z=''
l=0
dict_sample = {1:1, 2:2, 3:3,4:4, 5:5, 6:6,7:7, 8:8, 9:9}
state = [[dict_sample.get(1), dict_sample.get(2), dict_sample.get(3)],
         [dict_sample.get(4), dict_sample.get(5), dict_sample.get(6)],
         [dict_sample.get(7), dict_sample.get(8), dict_sample.get(9)]]

print("\n",state[0],"\n",state[1],'\n',state[2])
for i in range (0,9):
 if p==0 or p%2==0:
  z="0"
 else:
  z="x"
 x = input("Ввод ячейки")
 x = int(x)
 dict_sample[x] = z
 state = [[dict_sample.get(1),dict_sample.get(2), dict_sample.get(3)],[dict_sample.get(4),dict_sample.get(5), dict_sample.get(6)],[dict_sample.get(7),dict_sample.get(8), dict_sample.get(9)]]
 print("\n",state[0],"\n",state[1],'\n',state[2])
 p=p+1
 for u in range(0, 2):
  if state[u][0] == state[u][1] and state[u][1] == state[u][2]:
    print("win")
    sys.exit()
 for e in range(0,1):
  for h in range(0,1):
   for t in range(0,3):
    if state[e][t] == state[e+1][t] and state[e+1][t] == state[e+2][t]:
     print("win")
     sys.exit()
 for q in range(0,1):
  for j in range(0,1):
   if state[q][j]== state[q+1][j+1] and state[q+1][j+1] == state[q+2][j+2]:
    print("win")
    sys.exit()
   if state[q][j-1] == state[q + 1][j-2] and state[q + 1][j-2] == state[q + 2][j-3]:
    print("win")
    sys.exit()



