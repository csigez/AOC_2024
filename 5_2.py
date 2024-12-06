from collections import defaultdict, deque

def parse_input(filename):
    with open(filename, 'r') as f:
        content = f.read().strip()
    
    # Split into rules and updates sections
    rules_section, updates_section = content.split('\n\n')
    
    # Parse rules
    rules = defaultdict(list)
    for rule in rules_section.split('\n'):
        before, after = map(int, rule.split('|'))
        rules[before].append(after)
    
    # Parse updates
    updates = []
    for update in updates_section.split('\n'):
        pages = list(map(int, update.split(',')))
        updates.append(pages)
    
    return rules, updates

def is_valid_order(pages, rules):
    # For each page number that must come before others
    for i, page in enumerate(pages):
        if page in rules:
            # Check all pages that should come after this one
            for must_come_after in rules[page]:
                if must_come_after in pages:
                    # Find position of the page that must come after
                    after_pos = pages.index(must_come_after)
                    if after_pos <= i:  # If it comes before or at same position, order is invalid
                        return False
    return True

def build_graph(pages, rules):
    # Create adjacency list and in-degree count
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    
    # Initialize all pages with 0 in-degree
    for page in pages:
        in_degree[page] = 0
    
    # Build the graph for the current update
    for page in pages:
        if page in rules:
            for next_page in rules[page]:
                if next_page in pages:  # Only consider rules for pages in this update
                    graph[page].append(next_page)
                    in_degree[next_page] += 1
    
    return graph, in_degree

def topological_sort(pages, rules):
    graph, in_degree = build_graph(pages, rules)
    
    # Initialize queue with nodes that have no incoming edges
    queue = deque([page for page in pages if in_degree[page] == 0])
    result = []
    
    while queue:
        current = queue.popleft()
        result.append(current)
        
        # Process neighbors
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return result

def get_middle_number(pages):
    return pages[len(pages) // 2]

def solve_printer_problem_part2(filename):
    rules, updates = parse_input(filename)
    middle_sum = 0
    
    for update in updates:
        if not is_valid_order(update, rules):
            # Only process invalid updates
            correct_order = topological_sort(update, rules)
            middle_sum += get_middle_number(correct_order)
    
    return middle_sum

if __name__ == "__main__":
    result = solve_printer_problem_part2("5.txt")
    print(f"Sum of middle numbers from reordered invalid updates: {result}")