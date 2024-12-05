from collections import Counter

def calculate_total_distance(left_list, right_list):
    # Sort both lists
    left_sorted = sorted(left_list)
    right_sorted = sorted(right_list)
    
    # Calculate the total distance
    total_distance = sum(abs(l - r) for l, r in zip(left_sorted, right_sorted))
    return total_distance

def calculate_similarity_score(left_list, right_list):
    # Count occurrences of each number in the right list
    right_count = Counter(right_list)
    
    # Calculate similarity score
    similarity_score = sum(num * right_count[num] for num in left_list)
    return similarity_score

# Read numbers from 1.csv and store them in left_list and right_list
left_list = []
right_list = []

with open('1.csv', 'r') as file:
    for line in file:
        left, right = line.strip().split(';')
        left_list.append(int(left))
        right_list.append(int(right))

# Calculate total distance
result = calculate_total_distance(left_list, right_list)
print(f"Total distance: {result}")

result = calculate_similarity_score(left_list, right_list)
print(f"Similarity score: {result}")