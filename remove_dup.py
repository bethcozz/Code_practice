

unique = set()

with open('input.csv', 'r') as input_file, open('clean_input.csv', 'w') as clean_input_file:  

    for row in input_file.readlines()[1:]:
        id_ = row.strip()
        unique.add(id_)

    unique_list = sorted(list(unique))
    clean_input_file.write("causenumber\n")
    for item in unique_list:
        clean_input_file.write(item)



#set = only store one copy of anything - anytime you input the same string, it replaces (overwrites)
#for any string, assigns an address based on string 
