def verify(x):
    sorted_x = sorted(x)
    if x == sorted_x:
        return True
    return False

def verify_1(x):
    if len(x) ==0:
        return True
    current = x[0]
    for i in range(1,len(x)):
        print(current)
        print(x[i])
        print('------')
        if x[i] >= current:
            current = x[i]
        else:
            return False
    return True

def verify_rev(x):
    if len(x) == 0 or len(x) == 1:
        return True
    else:
        head = x[0]
        second = x[1]
        if head <= second:
            return verify_rev(x[1:])
        else:
            return False

def sort_alpha(x):
    result=[]
    while x:
        m = min(x)
        result.append(m)
        x.remove(m)
    return result

def mergesort(x):
    
    if len(x) == 0 or len(x) == 1:
        return x
    else:
        #divide
        head = x[:len(x)//2]
        tail = x[len(x)//2:]
        sorted_head = mergesort(head)
        sorted_tail = mergesort(tail)
        result = []
        #merge
        while sorted_head and sorted_tail:
            if sorted_head[0] <= sorted_tail[0]:
                result.append(sorted_head[0])
                sorted_head.remove(sorted_head[0])
            else:
                result.append(sorted_tail[0])
                sorted_tail.remove(sorted_tail[0])
            i += 1
        #when one part is empty
        if sorted_head:
            result += sorted_head
        else:
            result += sorted_tail
        return result
    


