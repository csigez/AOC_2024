def main():
    with open('11.txt', 'r') as f:
        input_data = f.read().split(" ")
    numbers = []
    for i in range(len(input_data)):
        numbers.append(int(input_data[i]))
    print(f"Initial numbers: {numbers}, and the length of the list is {len(numbers)}")
    
    blink = 0
    while blink < 75:
        if blink % 5 == 0:  # Show progress every 5 blinks
            print(f"Blink {blink}, Current number of stones: {len(numbers)}")
        
        i = 0
        while i < len(numbers):
            num = numbers[i]
            
            if num == 0:
                numbers[i] = 1
            else:
                # Check if number has even digits without converting to string
                digit_count = len(str(num))  # This is faster than log10 for our case
                if digit_count % 2 == 0:
                    # Split number mathematically
                    divisor = 10 ** (digit_count // 2)
                    right = num % divisor
                    left = num // divisor
                    numbers[i] = left
                    numbers.insert(i + 1, right)
                    i += 1
                else:
                    numbers[i] = num * 2024
            i += 1
        blink += 1
    
    print(f"Final number of stones after {blink} blinks: {len(numbers)}")

if __name__ == "__main__":
    main()