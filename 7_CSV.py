import datetime
import os
import csv

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

class Record:
    def __init__(self, text):
        self.text = text
        self.date = datetime.datetime.now()

class News(Record):
    def __init__(self, text, city):
        super().__init__(text)
        self.city = city

    def to_string(self):
        return f"News -------------------------\n{self.text}\n{self.city}, {self.date.strftime('%d/%m/%Y %H:%M')}\n"

class PrivateAd(Record):
    def __init__(self, text, expiration_date):
        super().__init__(text)
        self.expiration_date = expiration_date

    def to_string(self):
        days_left = (self.expiration_date - self.date).days
        return f"Private Ad  -------------------------\n{self.text}\nActual until: {self.expiration_date.strftime('%d/%m/%Y')}\nPublished on: {self.date.strftime('%d/%m/%Y')}\ndays left {days_left}\n"

class JokeOfTheDay(Record):
    def __init__(self, text):
        super().__init__(text)

    def to_string(self):
        return f"Joke of the day -------------------------\n{self.text}\nPublished on: {self.date.strftime('%d/%m/%Y %H:%M')}\n"

class NewsFeed:
    def __init__(self, file_name="6_feed.txt"):
        self.records = []
        self.file_name = file_name

    def preprocess_file(self,file_path):
        word_counts = {}
        #Tokenizing the text into words. Converting all words to lowercase. Counting the occurrences of each word.
        with open(file_path, 'r') as file:
            for line in file:
                words = line.strip().split()
                for word in words:
                    word = word.lower()
                    word_counts[word] = word_counts.get(word, 0) + 1
        return word_counts

    def create_word_count_csv(self, word_counts, csv_path):
        #Was concidered to count all set of symbols between spaces as a "word" for this task.
        with open(csv_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['word', 'count'])
            for word, count in word_counts.items():
                writer.writerow([word, count])

    def create_letter_statistics_csv(self, text, csv_path):
        letter_counts = {}
        total_letters = 0

        for letter in text:
            if letter.isalpha():
                total_letters += 1
                letter = letter.lower()
                letter_counts[letter] = letter_counts.get(letter, 0) + 1

        with open(csv_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['letter', 'count_all', 'count_uppercase', 'percentage'])
            for letter, count in letter_counts.items():
                uppercase_count = count if letter.isupper() else 0
                percentage = (count / total_letters) * 100
                writer.writerow([letter, count, uppercase_count, percentage])
 
    def publish_record(self, record):
        self.records.append(record)

    def read_feed(self):
        for record in self.records:
            print(record.to_string())

    def write_to_file(self, content):
        with open(self.file_name, "a") as file:
            file.write(content)
        word_counts = self.preprocess_file('6_feed.txt')
        # Create the word count CSV
        self.create_word_count_csv(word_counts, 'word_count.csv')
        # Read the 6_feed.txt file for letter statistics
        with open('6_feed.txt', 'r') as file:
            text = file.read()
        # Create the letter statistics CSV
        self.create_letter_statistics_csv(text, 'letter_statistics.csv')

class PublicationFromFile:
    def __init__(self, file_path="input_file.txt"):
        self.file_path = file_path

    def add_records_from_file(self, news_feed):
        try:
            with open(self.file_path, 'r') as f:
                lines = f.readlines()
                record_type = None
                text = None
                city = None
                expiration_date = None

                for line in lines:
                    line = line.strip()
                    if line.startswith("News -------------------------"):
                        record_type = "News"
                    elif line.startswith("Private Ad  -------------------------"):
                        record_type = "Private Ad"
                    elif line.startswith("Joke of the day -------------------------"):
                        record_type = "Joke of the day"
                    elif line.startswith("Text: "):
                        text = line[6:]
                    elif line.startswith("City: "):
                        city = line[6:]
                    elif line.startswith("Actual until: "):
                        expiration_date = datetime.datetime.strptime(line[14:], "%d/%m/%Y")
                    elif line.startswith("------"):
                        if record_type == "News":
                            news = News(text, city)
                            news_feed.publish_record(news)
                        elif record_type == "Private Ad":
                            private_ad = PrivateAd(text, expiration_date)
                            news_feed.publish_record(private_ad)
                        elif record_type == "Joke of the day":
                            joke = JokeOfTheDay(text)
                            news_feed.publish_record(joke)
                        text = None
                        city = None
                        expiration_date = None
        except FileNotFoundError:
            print("File not found.")
        else:
            os.remove(self.file_path)            

def main():
    news_feed = NewsFeed()

    while True:
        print("\nMenu:")
        print("1. Publish Record")
        print("2. Read Feed")
        print("3. Add Publications from File")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            print("\nSelect what to publish:")
            print("1. News")
            print("2. Advertisement")
            print("3. Joke of the day")

            publish_choice = input("Enter your choice (1/2/3): ")

            if publish_choice == '1':
                text = input("Enter news text: ")
                city = input("Enter city: ")
                news = News(normalize_cases(text), city)
                news_feed.publish_record(news)
                news_feed.write_to_file(news.to_string())
                print("News published successfully!")
            elif publish_choice == '2':
                text = input("Enter advertisement text: ")
                expiration_date = input("Enter expiration date (DD/MM/YYYY): ")
                expiration_date = datetime.datetime.strptime(expiration_date, "%d/%m/%Y")
                ad = PrivateAd(normalize_cases(text), expiration_date)
                news_feed.publish_record(ad)
                news_feed.write_to_file(ad.to_string())
                print("Advertisement published successfully!")
            elif publish_choice == '3':
                text = input("Enter joke text: ")
                joke = JokeOfTheDay(normalize_cases(text))
                news_feed.publish_record(joke)
                news_feed.write_to_file(joke.to_string())
                print("Joke published successfully!")
            else:
                print("Invalid choice.")
        elif choice == '2':
            news_feed.read_feed()
        elif choice == '3':
            file_path = input("Enter the file path (or press Enter to use default 'input_file.txt'): ").strip()
            if not file_path:
                file_path = "input_file.txt"
            file_handler = PublicationFromFile(file_path)
            file_handler.add_records_from_file(news_feed)
            print("Publications added successfully!")
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
