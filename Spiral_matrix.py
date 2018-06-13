'''
Created on Jun 12, 2018

@author: rajat.arora07
'''
def spiralNumbers(n):
    num=1
    row=int(n**0.5)
    col=row
    #print row,col
    
    #List for matirx.Initialized with all zeros.
    l1=[[0 for i in range(col)] for j in range(row)]
    
    #Current Direction is Right.
    dir='R'
    i=0
    j=0
    
    
    left_y=-1
    right_y=col
    down_x=row
    top_x=0
    #print l1
    
    while(num<=n):
        if dir=='R':
            while j<right_y:
                l1[i][j]=num
                j+=1
                num+=1
            if(num>n):
                break
            top_x=i
            j-=1
            i+=1
            dir='D'
            #print 'R',l1,num
        if dir=='D':
            while i<down_x:
                l1[i][j]=num
                i+=1
                num+=1 
            if(num>n):
                break
            dir='L'
            right_y=j
            i-=1
            j-=1
            #print 'D',l1,num
        if dir=='L':
            while j>left_y:
                l1[i][j]=num
                #print 'L inside',l1,j,left_y
                num+=1
                j-=1
            if(num>n):
                break
            down_x=i
            dir='U'
            j+=1
            i-=1
            #print 'L',l1,num
        if dir=='U':
            while i>top_x:
                l1[i][j]=num
                num+=1
                i-=1
            if(num>n):
                break
            left_y=j
            dir='R'
            j+=1
            i+=1
            #print 'U',l1,num
    print l1

#n=int input()
#n*=n
#spiralNumbers(25)