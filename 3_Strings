# Given text
input_text = """homEwork:​

tHis iz your homeWork, copy these Text to variable. ​

​

You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.​

​

it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. ​

​

last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.​"""

# Normalize the text
result = []#list of characters for 
capitalize_next = True  # Flag to capitalize the next character
space_count = 0 #to count whitespaces
last_word_flag = False
last_word = []
last_words = []

for char in input_text:
    if char.isspace(): 
       #count spaces - if char is space we increment counter, adding char to resulting string and continiue
       space_count += 1
       result.append(char)
       #last words - if it is first space after another one space - reset last word. Otherwise, start to check a new one if it is last word in a sentance. 
       if last_word_flag == False:
        last_word_flag = True
       else:
          last_word = []
    elif char == '\u200b': 
        #normilize cases - hendler for zero-width-space. Do not count into space count but do not capitalize, but capitailize next instead
        capitalize_next = True
        result.append(char)
    elif char in ['.', '!', '?']:
        #normilize cases - if char is end-of-sentence character we trigger flag to capitalize next non-space character
        capitalize_next = True
        result.append(char)
        #last words - add last word of the sentance into variable.
        last_words.extend([' '] + last_word)
        last_word_flag = False
    elif capitalize_next:
        #normilize cases - capitilize first letter of the sentance. 
        result.append(char.upper())
        capitalize_next = False        
        #last words - in case we will have 1 word sentance
        if len(last_word) == 0:
            last_word.append(char.upper())
        else:
            last_word.append(char.lower())
    else:
        #normilize cases - add lowercase character
        result.append(char.lower())
        #last words - if we do not have cached words and didn't started chachin new word we capitilize first letter to cache. 
        if len(last_words) == 0 and len(last_word) == 0:
            last_word.append(char.upper())
        else:
            last_word.append(char.lower())

normalized_text = ''.join(result)
added_sentance = ''.join(last_words)

# Fix misspelling "iZ" with correct "is". 
normalized_text = normalized_text.replace(" iz ", " is ")

# Add sentence with last words of each existing sentence in the end of the second paragraph. 
paragraphs = normalized_text.split('\n\n\u200b\n\n')

if len(paragraphs) >= 2:
    paragraphs[1] +=  added_sentance

normalized_text = '\n\n\u200b\n\n'.join(paragraphs)

print(normalized_text)

#count spaces
print("\nNumber of whitespace characters is", space_count)
