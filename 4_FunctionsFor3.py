# Given text
input_text = """homEwork:​

tHis iz your homeWork, copy these Text to variable. ​

​

You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.​

​

it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. ​

​

last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.​"""

def convert_last_words_to_sentence(my_text):

    last_word_flag = False
    last_word = []
    last_words = []

    for char in my_text:
        if char.isspace(): 
        #last words - if it is first space after another one space - reset last word. Otherwise, start to check a new one if it is last word in a sentance. 
            if last_word_flag == False:
                last_word_flag = True
            else:
                last_word = []
        elif char in ['.', '!', '?']:
            #last words - add last word of the sentance into variable.
            last_words.extend([' '] + last_word)
            last_word_flag = False
        else:
            #last words - if we do not have cached words and didn't started chachin new word we capitilize first letter to cache. 
            if len(last_words) == 0 and len(last_word) == 0:
                last_word.append(char.upper())
            else:
                last_word.append(char.lower())   
    return  ''.join(last_words)

def normalize_cases(text):     
    # Normalize the text
    result = []#list of characters for 
    capitalize_next = True  # Flag to capitalize the next character

    for char in text:
        if char.isspace(): 
            result.append(char)
        elif char == '\u200b': 
            #normilize cases - hendler for zero-width-space. Do not count into space count but do not capitalize, but capitailize next instead
            capitalize_next = True
            result.append(char)
        elif char in ['.', '!', '?']:
            #normilize cases - if char is end-of-sentence character we trigger flag to capitalize next non-space character
            capitalize_next = True
            result.append(char)
        elif capitalize_next:
            #normilize cases - capitilize first letter of the sentance. 
            result.append(char.upper())
            capitalize_next = False        
        else:
            #normilize cases - add lowercase character
            result.append(char.lower())

    return ''.join(result)

def count_spaces(text):
    space_count = 0
    for char in text:
        if char.isspace(): 
        #count spaces - if char is space we increment counter, adding char to resulting string and continiue
            space_count += 1
    return space_count

def add_text_to_paragraph(text, sentence, paragraph_no):
    # Add sentence in the end of the text's paragraph. 
    paragraphs = text.split('\n\n\u200b\n\n')

    if len(paragraphs) >= paragraph_no - 1:
        paragraphs[paragraph_no - 1] +=  sentence

    text = '\n\n\u200b\n\n'.join(paragraphs)

    return text

def replace_EZ_to_IS(input):
  return input.replace(" iz ", " is ")


normalized_text = normalize_cases(input_text)

normalized_text = replace_EZ_to_IS(normalized_text)

sentence = convert_last_words_to_sentence(input_text)

normalized_text = add_text_to_paragraph(normalized_text, sentence, 1)

space_count = count_spaces(input_text)

print(normalized_text)

#count spaces
print("\nNumber of whitespace characters is", space_count)
