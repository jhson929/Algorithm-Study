def solution(s):
    li = [ss for ss in s]
    li.sort(reverse = True)
    
    return "".join(li)