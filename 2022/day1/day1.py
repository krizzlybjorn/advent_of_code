input_data = open("input", "r")

elf_list = []
elf_temp = 0

for line in input_data:
    line = line.replace('\n', '')
    if line == "":
        elf_list.append(elf_temp)
        elf_temp = 0
    else:
        elf_temp += int(line)

print(max(elf_list))

elf_top_three = elf_list
elf_top_three.sort()
elf_top_three = elf_top_three[-3:]
print(sum(elf_top_three))
