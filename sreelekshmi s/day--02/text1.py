"""Text = “created my first program in research zlight”

Replace the text “first” to “second”
Swap the words research and zlight
Displayed as”Created my second program in Zlight Research Pvt Ltd”. """



Text1="created my first program in research zlight"
Text2=" Pvt Ltd "
Text=Text1 + Text2                      #concatenation of two string
Text=Text.replace("first" , "second")     #replace the words 
words = Text.split()                #split the words
words[0],words[5], words[6] = words[0].capitalize(),words[6].capitalize(), words[5].capitalize()   # swap research and zlight  and capitalize
new_Text = " ".join(words)
print(new_Text)


