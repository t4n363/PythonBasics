import random

# Step 1: Create a list containing from 2 to 10 items. Each element of the list is a dictionary of random numbers. 
list_of_dicts = []
num_of_dicts = random.randint(2, 10)

for i in range(num_of_dicts):
    num_of_keys = random.randint(1, 5)  # Define how many elements will be in the dictionary (1 to 5)
    new_dict = {}
    
    #Dictionary elements are random numbers from 0 to 100. Dictionary key is a random letter. 
    for j in range(num_of_keys):
        key = chr(random.randint(97, 122))  # Random lowercase letter (ASCII 97 to 122)
        value = random.randint(0, 100)      # Random number (0 to 100)
        new_dict[key] = value
    
    list_of_dicts.append(new_dict)

print("List of dictionaries:")
for idx, d in enumerate(list_of_dicts, start=1):
    print(f"Dict {idx}: {d}")

# Step 2: Create a common dictionary from previously generated dictionaries. 
common_dict = {}

for idx, d in enumerate(list_of_dicts, start=1):
    for key, value in d.items():
        if key in common_dict:
            if value > common_dict[key]: #If dicts have same key, we will take max value, and rename key with dict number with max value.
                common_dict[f"{key}_{idx}"] = value 
                del common_dict[key] 
        else:
            common_dict[key] = value #If key is only in one dict - take it as is.

print("\nCommon dict:")
print(common_dict)
