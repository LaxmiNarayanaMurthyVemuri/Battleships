def mostCommFirstLetter(s):
    count = 0
    for i in range(0, len(s)):
        if s[i] == ' ':
            letter = s[i+1]
            count = 1
            for j in range(i+1, len(s)):
                if s[j] == ' ':
                    letter1 = s[j+1]
                    if(letter == letter1):
                        count += 1 
                        return count
            
    
print(mostCommFirstLetter("do you have a voting plan for the election happening next month"))


