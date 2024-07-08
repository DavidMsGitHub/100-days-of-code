with open("file1.txt", "r") as file1:
    output = file1.readlines()
    file1_numbers = [int(num.strip("\n")) for num in output]

with open("file2.txt", "r") as file2:
    output = file.readlines()
    file1_numbers = [int(num.strip("\n")) for num in output]

print(file1_numbers)


# result = []
# # Write your code above 👆
#
# print(result)


