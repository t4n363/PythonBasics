import datetime
import sqlite3

class Publication:
    def __init__(self, publication_type, publication_text, publication_city=None, publication_expiration=None):
        self.publication_type = publication_type
        self.publication_text = self.normalize_text(publication_text)
        self.publication_city = publication_city
        self.publication_date = datetime.datetime.now().strftime('%d/%m/%Y %H:%M')
        self.publication_expiration = publication_expiration

    def normalize_text(self, text):   
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

    def format_for_file(self):
        if self.publication_type == "News":
            return f"News -------------------------\n{self.publication_text}\n{self.publication_city}, {self.publication_date}\n-------------------------"
        elif self.publication_type == "Advertisement":
            return f"Private Ad  -------------------------\n{self.publication_text}\nActual until: {self.publication_expiration}\nPublished on: {self.publication_date}\nDays valid: {self.calculate_days_valid()}-------------------------"
        elif self.publication_type == "Joke of the day":
            return f"Joke of the day -------------------------\n{self.publication_text}\nActual until: {self.calculate_expiration_date()}\n{self.publication_city}, {self.publication_date}\n-------------------------"
        else:
            return ""

    def format_for_db(self):
        return (
            self.publication_type,
            self.publication_text,
            self.publication_city,
            self.publication_date,
            self.publication_expiration
        )

    def calculate_days_valid(self):
        expiration_date = datetime.datetime.strptime(self.publication_expiration, '%d/%m/%Y')
        current_date = datetime.datetime.now()
        return (expiration_date - current_date).days

    def calculate_expiration_date(self):
        current_date = datetime.datetime.now()
        expiration_date = current_date + datetime.timedelta(days=1)
        return expiration_date.strftime('%d/%m/%Y')
