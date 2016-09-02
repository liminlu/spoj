a= input()
for k in range(a):
    line, column = map(int, raw_input().split())
   
    for i in range(line):
        if (i%2 ==0):
            j=column/2
            if (column%2 == 0):
                print  "*." * j
            else: 
                 print  "*." * j + "*"
        else:
            j=column/2
            if (column%2 == 0):
                print  ".*" * j
            else: 
                 print  ".*" * j + "."
    print " "*column
          

    
    
    
    
    
    
    
