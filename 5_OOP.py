import datetime

class NewsFeed:
    def __init__(self): #constructor that initialize file_path when instance of class created.
        self.file_path = "5_news_feed.txt"
    
    def publish_record(self):
        print("Select what to publish:")
        print("1. News")
        print("2. Advertisement")
        print("3. Advertorial")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            text = input("Enter news text: ")
            city = input("Enter city: ")
            self._append_to_file("News", text, city)
        elif choice == '2':
            text = input("Enter advertisement text: ")
            expiration_date = input("Enter expiration date (DD/MM/YYYY): ")
            self._append_to_file("Private Ad", text, expiration_date)
        elif choice == '3':
            text = input("Enter advertorial text: ")
            city = input("Enter city: ")
            expiration_date = input("Enter expiration date (DD/MM/YYYY): ")
            self._append_to_file("Advertorial", text, expiration_date, city)
        else:
            print("Invalid choice.")
    
    def _append_to_file(self, record_type, text, *args):
        with open(self.file_path, 'a') as f:
            f.write(f"{record_type} {'-' * 25}\n")
            f.write(f"Text: {text}\n")
            
            if record_type != "News":
                expiration_date = datetime.datetime.strptime(args[0], "%d/%m/%Y")
                f.write(f"Actual until: {args[0]}\n")
                current_date = datetime.datetime.now().strftime("%d/%m/%Y")
                f.write(f"Published on: {current_date}\n")
                days_left = (expiration_date - datetime.datetime.now()).days
                f.write(f"Days left: {days_left}\n")
            
            if record_type == "News" or record_type == "Advertorial":
                f.write(f"City: {args[-1]}, {datetime.datetime.now():%d/%m/%Y %H:%M}\n")
            
            f.write("------\n")
    
    def read_feed(self):
        try:
            with open(self.file_path, 'r') as f:
                content = f.read()
                print(content)
        except FileNotFoundError:
            print("No records found in the news feed.")

def main():
    news_feed = NewsFeed()
    
    while True:
        print("1. Publish Record")
        print("2. Read Feed")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            news_feed.publish_record()
        elif choice == '2':
            news_feed.read_feed()
        elif choice == '3':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
