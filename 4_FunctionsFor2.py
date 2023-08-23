def create_list_of_dicts():

    import random

    #Create a list containing from 2 to 10 items. Each element of the list is a dictionary of random numbers. 
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

    return list_of_dicts

list_of_dicts = create_list_of_dicts()

print("List of dictionaries:")
for idx, d in enumerate(list_of_dicts, start=1):
    print(f"Dict {idx}: {d}")


def merge_dicts_by_key(input_list_of_dicts):

    if len(input_list_of_dicts) < 2:
        return input_list_of_dicts

    common_dict = {}
    # Create a common dictionary from input list of dicts generated dictionaries. 

    for idx, d in enumerate(input_list_of_dicts, start=1):
        for key, value in d.items():
            if key in common_dict:
                if value > common_dict[key]: #If dicts have same key, we will take max value, and rename key with dict number with max value.
                    common_dict[f"{key}_{idx}"] = value 
                    del common_dict[key] 
            else:
                common_dict[key] = value #If key is only in one dict - take it as is.

    return common_dict

common_dict = merge_dicts_by_key(list_of_dicts)
print("\nCommon dict:")
print(common_dict)
