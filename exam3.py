#Input to handle : (1) Binary drone files + (2) Text file with plant names

#1. Read all files
# ask the user for no. of drone files

#2. Process data from drones
# Take: plants each drone detected
# All unique plants detected
# Plants detected by several drones

# 3. Display results 
# Show: Plants for each drone;
# All unique plants detected
# Plants detected by several drones
# The name of all detected plants 

import pickle

def read_drone_file(filename):
    # Read binary (serialized) file specified by *filename*
    # Return the set stored in the file. 
    # The set contains tuples storing the location (x, y) for each plant identified as problematic.
    with open(filename.pickle, 'rb') as file:
        data = pickle.load(file)
    return data

def read_plant_register(filename):
    plant_dict = {}
    with open (filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) == 3:
                X = int(parts[0].strip())
                Y = int(parts[1].strip())
                NAME = parts[2].strip()
                plant_dict[(X, Y)] = NAME
    return plant_dict
    # Create dictionary using the data in the text file *filename*
    # Return afformentioned
    # Each line has the format: "X,Y,NAME"
    # Where X and Y are the location 
    # Where NAME is the str of the plant
    # where the key shall be a tuple and the value shall be a string. 
    # The tuple used for the key shall be constructed using X and Y but converted to integer values, and the value is the NAME.


def filter_one_of_each(data_sets):
    unique_tuples = set()
    for dataset in data_sets:
        unique_tuples.update(dataset)
    return unique_tuples
    # given a list of sets *data_sets* shall return a new set that contains a unique copy of all tuples
    # eg. Input:
    #{(1, 2), (3, 4)}, {(3, 4), (5, 6)} ]
    # eg. output
    #{ (1,2), (3, 4), (5, 6) }

def filter_detected_by_several(data_sets):
    tuple_count = {}
    for dataset in data_sets:
        for tuple_item in dataset:
            if tuple_item in tuple_count:
                tuple_count[tuple_item] += 1
            else:
                tuple_count[tuple_item] = 1
    result_set = {tuple_item for tuple_item, count in tuple_count.items() if count > 1}
    return result_set
    #shall return a new set containing only the tuples that occurs in more than one of the sets in the list data_sets. 
    #eg. Input:
    #[ {(1, 2), (3, 4)}, {(3, 4), (5, 6)} ]
    #eg. Output:
    #{ (3, 4) }

def print_set(data):
    sorted_list = sorted(data)
    count = 0
    for element in sorted_list:
        print(f"{element:<15}", end="")
        count += 1
        if count % 5 == 0:
            print()
    if count % 5 != 0:
        print()
    #convert data into list using sorted()
    #print all elements after
    #Only five elements shall be printed on each line before doing a line break
    #each element from the list shall be printed using a minimum width of 15 characters and shall be left aligned. 

def print_with_translation(data, translation_dict):
    translated_list = []
    for element in data:
        translated_value = translation_dict.get(element, 'Unknown')
        translated_list.append(translated_value)
    sorted_list = sorted(translated_list)
    count = 0
    for element in sorted_list:
        print(f"{element:<15}", end="")
        count += 1
        if count % 5 == 0:
            print()
    if count % 5 != 0:
        print()

def print_results(data_sets, translation_dict):
    number_of_drones = 3 - 1 #example (need -1)
    count = 0
    if count != number_of_drones:
        for count in number_of_drones:
            print(f"Plants detected by drone {count}:")
            print("x") #fill in
            count +=1
    print(f"List of all detected plants:\n")

    print(f"Plants detected by several drones:\n")

    print(f"Plants listed by name/ID:\n")


def main():
    number_of_drones = input("How many drones are there?")
    print(results())
    #ask the user how many drones
    #create a loop that reads a set from each drone and places in list
    #filenames follow the format "drone_data_xxx.dat" where xxx is a counter that starts at zero and increases by one for each file read
    #Create a translation dictionary that given a location (x, y) as key returns a human friendly description of the plant at that location. The data needed to create the dictionary will always be found in a file named "plant_register.txt". The key shall be a tuple consisting of two integer values and the value shall be a string
    #print a summary
    pass    

if __name__ == '__main__':
    main()