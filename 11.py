from collections import deque

def main():
    with open('11.txt', 'r') as f:
        input_data = f.read().split(" ")
    
    # Use deque for faster insertions
    numbers = deque(int(x) for x in input_data)
    print(f"Initial numbers: {list(numbers)}")
    
    blink = 0
    while blink < 75:
        if blink % 5 == 0:
            print(f"Blink {blink}, stones: {len(numbers)}")
        
        size = len(numbers)
        for _ in range(size):
            num = numbers.popleft()
            
            if num == 0:
                numbers.append(1)
            else:
                digit_count = len(str(num))
                if digit_count % 2 == 0:
                    divisor = 10 ** (digit_count // 2)
                    left = num // divisor
                    right = num % divisor
                    numbers.append(left)
                    numbers.append(right)
                else:
                    numbers.append(num * 2024)
        
        blink += 1
    
    print(f"Final number of stones after {blink} blinks: {len(numbers)}")

if __name__ == "__main__":
    main()