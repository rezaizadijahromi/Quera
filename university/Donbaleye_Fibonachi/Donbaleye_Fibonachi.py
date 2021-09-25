n = int(input())
m = int(input())
print(n)

def ShowFibNth(n,m):
    if n==1 and m==1:
        return None
    else:
        print(m-n)
        b=n
        a = m-n
        return ShowFibNth(a,b)
        
ShowFibNth(n,m)
    

        
        
    
    
    
 
    
    
    
    

    
    
        
        
            
            
        


    
    
    
    

    
    
        
        
            
            
        

