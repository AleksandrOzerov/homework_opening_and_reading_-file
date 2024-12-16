import os

file_names = ["1.txt", "2.txt", "3.txt"]
files_content = {}
for file_name in file_names:
    with open(file_name, encoding="utf-8") as f:
        files_content[file_name] = f.readlines()
sorted_files = sorted(files_content.items(), key=lambda x: len(x[1]))
output_filename = "result.txt"
with open(output_filename, "w", encoding="utf-8") as output_file:
    for file_name, content in sorted_files:
        output_file.write(f"{file_name}\n{len(content)}\n")
        output_file.writelines(content)
        output_file.write("\n")

print(f"Результат сохранен в файл {output_filename}.")
with open('result.txt', 'r', encoding='utf-8') as file:
    content = file.read()

print(content)