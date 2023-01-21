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

while True:
    binary_string = ''.join(map(str, binary_statement))
    character = chr(int(binary_string, 2))
    # return the stream of characters
    yield character
