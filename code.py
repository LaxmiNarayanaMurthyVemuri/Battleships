def mostCommFirstLetter(s):
    count = 0
    print(s[0])
    for i in range(0, len(s)):
        print(s[i])
        for j in range(i+1, len(s)):
            if(s[i] == s[j] and s[i] != ' '):
                count = count + 1  
                print("Char:", s[i], "Count:", count+1)
            
    if(count > 1 and s[i] != '0'):  
        print(s[i]);  
    
print(mostCommFirstLetter("Name is Naina"))