# PythonBasics
Collection of simple scripts

1_BasicPythonOperators.py
File contains solution for a simple task: 
create list of 100 random numbers from 0 to 1000
sort list from min to max (without using sort())
calculate average for even and odd numbers
print both average result in console 

2_Collections.py
File contains solution for a simple task for generationa and work with collections in Python.
1. Create a list of random number of dicts (from 2 to 10)
Dict's random numbers of keys should be letter,
Dict's values should be a number (0-100),
example: [{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]
2. Get previously generated list of dicts and create one common dict:
If dicts have same key, we will take max value, and rename key with dict number with max value
If key is only in one dict - take it as is,
Example: {'a_1': 5, 'b': 7, 'c': 35, 'g_2': 42}

3_Strings.py
Solition of second homework. 
1. Normilize cases for a given text. 
2. Count spaces.
3. Create sentensce from the last word of the existing sentences. Add it to the end of second paragraph.  

4_FunctionsFor2.py
Module contains homework2 decompositioned into functions.

4_FunctionsFor3.py
Module contains homework3 decompositioned into functions.

5_OOP.py
File contains simple console tool to read from file and write into file feed from user input. 

6_Module.py 
Homework 5 extended with publication from file. 

7_CSV.py
Homework 6 extended with methods to create 2 files with statistics for feed.
First file letter_statistics.csv contains cout of letter in the file, count uppercase, percentage this of letter in a text. 
Second file contains each word and amount of the word in a file. As word concidered set of symbols between 2 spaces. 

final_task_calculate_distance.py
Tool which calculate straight-line distance between different cities based on coordinates:
 1. User will provide two city names by console interface
 2. If city coordinates not in DB, it will ask user for input and store it in SQLite database for future use
 3. Return distance between cities in kilometers