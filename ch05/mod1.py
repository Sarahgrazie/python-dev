def sum(a,b):
    return a+ b 

def safe_sum(a,b):
    if type(a) != type(b):
        print('type is wrong')
        return
    else:
        return sum(a,b)
    
if __name__ == '__main__': # vital 
#function test code
print(sum(1,1))
print(safe_sum('a',1))
print(sum(10,10.4))