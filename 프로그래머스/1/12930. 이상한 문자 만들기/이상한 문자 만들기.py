def solution(s):
    words = s.split(" ")
    new_words = []
    
    for w in words:
        i = 0
        new_word = ""
        
        while i < len(w):
            if i % 2 == 0:
                new_word += w[i].upper()
            else:
                new_word += w[i].lower()
            
            i += 1
        
        new_words.append(new_word)
        
    answer = " ".join(new_words)
    return answer