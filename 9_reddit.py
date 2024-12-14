import sys


def checksum(disk):
    return sum([i * n for i, n in enumerate(disk) if n >= 0])


def solve_p1(fs, files, free_space):
    while free_space[0] <= files[-1]:
        i, j = files[-1], free_space[0]
        fs[i], fs[j] = fs[j], fs[i]
        del files[-1]
        del free_space[0]
    return fs


def solve_p2(fs, files, free_space):
    for file, file_len in files[::-1]:
        for i, (free, free_len) in enumerate(free_space):
            if file_len <= free_len and file > free:
                for j in range(file_len):
                    fs[free + j], fs[file + j] = (
                        fs[file + j],
                        fs[free + j],
                    )
                free_space[i] = (free + file_len, free_len - file_len)
                break
    return fs


data = open("9.txt", "r").read().strip()
disk_map = [int(n) for n in data]

fs = []
files_p1, free_space_p1 = [], []
files_p2, free_space_p2 = [], []
file = True
cur = 0
for l in disk_map:
    if file:
        files_p1.extend(i for i in range(len(fs), len(fs) + l))
        files_p2.append((len(fs), l))
        fs.extend([cur] * l)
        cur += 1
    else:
        free_space_p1.extend(i for i in range(len(fs), len(fs) + l))
        free_space_p2.append((len(fs), l))
        fs.extend([-1] * l)
    file = not file

p1 = solve_p1(fs[::], files_p1, free_space_p1)
p2 = solve_p2(fs[::], files_p2, free_space_p2)

print(f"Part 1: {checksum(p1)}")
print(f"Part 2: {checksum(p2)}")