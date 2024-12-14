def create_blocks(input_data):
    output = ""
    badge_id = 0
    print("Solution for part1:")
    for i, char in enumerate(input_data):
        if i % 2 == 0:
            j = 0
            while j < int(char):
                output = output + str(badge_id)
                j = j + 1
            badge_id = badge_id + 1
        else:
            j = 0
            while j < int(char):
                output = output + "."
                j = j + 1
    return output

def move_file_blocks(input_data):
    output = list(input_data)  
    last_pos = len(output)-1
    for i in range(len(output)):
        if output[i] == ".":
            while last_pos >= i and output[last_pos] == ".":
                last_pos = last_pos - 1
            if last_pos >= i:
                # print(f"Moving {output[last_pos]} from {last_pos} to {i}")
                output[i] = str(output[last_pos])
                output[last_pos] = "."
                # print(output)
                last_pos = last_pos - 1

    return "".join(output) 

def calc_checksum(input_data):
    output = 0
    for i in range(len(input_data)):
        if input_data[i] != ".":
            output += i*(int(input_data[i]))
            # print(f"i is {i}, and char is {input_data[i]}")
    return output

def main():
    with open('input_Miki.txt', 'r') as f:
        input_data = f.read()
    test_input = "2333133121414131402"
    blocks = create_blocks(input_data)
    blocks = move_file_blocks(blocks)
    print(calc_checksum(blocks))

if __name__ == "__main__":
    main()