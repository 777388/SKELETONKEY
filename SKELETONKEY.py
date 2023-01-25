import multiprocessing

# Create a shared memory array to store the binary statement
binary_statement = multiprocessing.Array('i', [0,0,0,0,0,0,0,0])

def toggle_bit(thread_id):
    while True:
        binary_statement[thread_id] = 1 - binary_statement[thread_id]


# Create the processes
processes = []
for i in range(8):
    process = multiprocessing.Process(target=toggle_bit, args=(i,))
    process.start()
    processes.append(process)

def onechar():
    while True:
        binary_string = ''.join(map(str, binary_statement))
        character = chr(int(binary_string, 2))
        return character

# Create an empty list to store the characters
characters_list = []
while True:
    # Create a list of 8 characters
    characters = [onechar() for _ in range(8)]
    # Check if the characters already exist in the list
    if ''.join(characters) not in characters_list:
        characters_list.append(''.join(characters))
        # Print the characters as a single string
        print(''.join(characters))
