a= input()
for k in range(a):
    line, column = map(int, raw_input().split())
   
    for i in range(line):
        if (line <3 or column <3):
           print "*" * column
        else:
           if(i==0):
               print "*" * column
           elif(i ==(line-1)):   
               print "*" * column
           else:
               print "*"+"."* (column -2)+"*"
    print " "*column
