from collections import defaultdict

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

def get_middle_number(pages):
    return pages[len(pages) // 2]

def solve_printer_problem(filename):
    rules, updates = parse_input(filename)
    middle_sum = 0
    
    for update in updates:
        if is_valid_order(update, rules):
            middle_sum += get_middle_number(update)
    
    return middle_sum

if __name__ == "__main__":
    result = solve_printer_problem("5.txt")
    print(f"Sum of middle numbers from valid updates: {result}")