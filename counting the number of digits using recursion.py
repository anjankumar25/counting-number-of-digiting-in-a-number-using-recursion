def aa(a):
    
    if a == 0:
        return 0
    v=0
    e=a%10
    if e >=1 and e<=9:
        v=v+1
    
        
    return v + aa(a//10)
    
print(aa(789))