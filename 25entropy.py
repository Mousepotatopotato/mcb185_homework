import math

def entropy(a, c, g, t):
    length = a + c + g + t
    if length != 0:
        p_a = a/length
        p_c = c/length
        p_g = g/length
        p_t = t/length
    
    if a + c + g + t == 0:
        return 0
    
    elif a + c + g == 0:
        return -1*p_t*math.log(p_t, 2)*t
        
    elif a + c + t == 0:
        return -1*p_g*math.log(p_g, 2)*g
        
    elif a + t + g == 0:
        return -1*p_c*math.log(p_c, 2)*c

    elif c + t + g == 0:
        return -1*p_a*math.log(p_a, 2)*a
            
    elif a + c == 0:
        return -1*(p_t*math.log(p_t, 2)*t + p_g*math.log(p_g, 2)*g)
    
    elif a + g == 0:
        return -1*(p_t*math.log(p_t, 2)*t + p_c*math.log(p_c, 2)*c)
    
    elif a + t == 0:
        return -1*(p_c*math.log(p_c, 2)*c + p_g*math.log(p_g, 2)*g)
    
    elif c + g == 0:
        return -1*(p_t*math.log(p_t, 2)*t + p_a*math.log(p_a, 2)*a)
    
    elif c + t == 0:
        return -1*(p_a*math.log(p_a, 2)*a + p_g*math.log(p_g, 2)*g)
    
    elif t + g == 0:
        return -1*(p_a*math.log(p_a, 2)*a + p_c*math.log(p_c, 2)*c)
    
    elif a == 0:
        return -1*(p_t*math.log(p_t, 2)*t + p_g*math.log(p_g, 2)*g + p_c*math.log(p_c, 2)*c)
    
    elif c == 0:  
        return -1*(p_t*math.log(p_t, 2)*t + p_g*math.log(p_g, 2)*g + p_a*math.log(p_a, 2)*a)
    
    elif g == 0:
        return -1*(p_t*math.log(p_t, 2)*t + p_a*math.log(p_a, 2)*a + p_c*math.log(p_c, 2)*c)
    
    elif t == 0:
        return -1*(p_a*math.log(p_a, 2)*a + p_g*math.log(p_g, 2)*g + p_c*math.log(p_c, 2)*c)
    
    else:
        return -1* ((p_t * math.log(p_t, 2))*t + (p_c * math.log(p_c, 2)) * c + (p_g * math.log(p_g, 2))* g + (p_a * math.log(p_a, 2))*a)

print(entropy(1,1,1,1))
print(entropy(0,1,1,1))
print(entropy(0,0,0,0))
print(entropy(12,17,12,15))
