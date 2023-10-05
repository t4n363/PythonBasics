import os
from publication import Publication
import sqlite3
import xml.etree.ElementTree as ET

def publish_record():
    print("Select the type of publication:")
    print("1. News")
    print("2. Advertisement")
    print("3. Joke of the day")

    publication_type = input("Enter your choice (1/2/3): ")
    publication_text = input("Enter the publication text: ")

    if publication_type == "1":
        city = input("Enter the city: ")
        publication = Publication("News", publication_text, city)
    elif publication_type == "2":
        expiration_date = input("Enter the expiration date (DD/MM/YYYY): ")
        publication = Publication("Advertisement", publication_text, None, expiration_date)
    elif publication_type == "3":
        city = input("Enter the city: ")
        publication = Publication("Joke of the day", publication_text, city)
    else:
        print("Invalid choice. Publication not created.")
        return

    # Write to file
    with open("news_feed.txt", "a") as file:
        file.write(publication.format_for_file())

    # Insert into database
    conn = sqlite3.connect('db_feed.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO t_news_feed (publication_type, publication_text, publication_city, publication_date, publication_expiration) VALUES (?, ?, ?, ?, ?)', publication.format_for_db())
    conn.commit()
    conn.close()

    print("Publication added successfully.")

def read_feed():
    print("Select the source to read from:")
    print("1. Read from file")
    print("2. Read from database")

    source = input("Enter your choice (1/2): ")

    if source == "1":
        try:
            with open("news_feed.txt", "r") as file:
                print(file.read())
        except FileNotFoundError:
            print("The file 'news_feed.txt' does not exist.")
    elif source == "2":
        conn = sqlite3.connect('db_feed.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM t_news_feed')
        publications = cursor.fetchall()
        conn.close()

        for publication in publications:
            print(publication)
    else:
        print("Invalid choice. Feed not read.")

def add_publications_from_file():
    print("Select the file type to add publications from:")
    print("1. Flat file")
    print("2. JSON")
    print("3. XML")

    file_type = input("Enter your choice (1/2/3): ")

    if file_type == "1":
        file_name = input("Enter the file name (or press Enter to use default 'input_news_feed.txt'): ")
        if not file_name:
            file_name = "input_news_feed.txt"
        
        add_publications_from_flat_file(file_name)
    elif file_type == "2":
        file_name = input("Enter the file name (or press Enter to use default 'input_news_feed.json'): ")
        if not file_name:
            file_name = "input_news_feed.json"

        add_publications_from_json(file_name)
    elif file_type == "3":
        file_name = input("Enter the file name (or press Enter to use default 'input_news_feed.xml'): ")
        if not file_name:
            file_name = "input_news_feed.xml"

        add_publications_from_xml(file_name)
    else:
        print("Invalid choice. Publications not added.")

def add_publications_from_flat_file(file_name):
    try:
        with open(file_name, "r") as file:
            lines = file.readlines()
            for i in range(0, len(lines), 4):
                publication_type = lines[i].strip()
                publication_text = lines[i+1].strip()
                publication_city = lines[i+2].strip()
                publication_date = datetime.datetime.now().strftime('%d/%m/%Y %H:%M')
                if publication_type == "Advertisement":
                    publication_expiration = lines[i+3].strip().split(": ")[1]
                else:
                    publication_expiration = None
                
                publication = Publication(publication_type, publication_text, publication_city, publication_expiration)

                # Write to file
                with open("news_feed.txt", "a") as output_file:
                    output_file.write(publication.format_for_file())

                # Insert into database
                conn = sqlite3.connect('db_feed.db')
                cursor = conn.cursor()
                cursor.execute('INSERT INTO t_news_feed (publication_type, publication_text, publication_city, publication_date, publication_expiration) VALUES (?, ?, ?, ?, ?)', publication.format_for_db())
                conn.commit()
                conn.close()

        print("Publications added successfully.")
        os.remove(file_name)  # Remove the file after loading

    except FileNotFoundError:
        print(f"The file '{file_name}' does not exist.")

def add_publications_from_json():
    file_name = input("Enter the JSON file name or path (leave blank for default): ")

    if not file_name:
        file_name = "input_news_feed.json"

    try:
        with open(file_name, 'r') as file:
            data = json.load(file)

            for item in data:
                publish_record(item['type'], item['text'], item['city'], item['expiration'])
    except FileNotFoundError:
        print(f"The file '{file_name}' does not exist.")


def add_publications_from_xml():
    file_name = input("Enter the XML file name or path (leave blank for default): ")

    if not file_name:
        file_name = "input_news_feed.xml"

    try:
        tree = ET.parse(file_name)
        root = tree.getroot()

        for publication in root:
            type = publication.find('type').text
            text = publication.find('text').text
            city = publication.find('city').text
            expiration = publication.find('expiration').text

            publish_record(type, text, city, expiration)
    except FileNotFoundError:
        print(f"The file '{file_name}' does not exist.")


# Main program
if __name__ == "__main__":
    while True:
        print("\nMenu:")
        print("1. Publish record")
        print("2. Read feed")
        print("3. Add publications from file")
        print("4. Exit")
