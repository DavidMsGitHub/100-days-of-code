directory = "../../../Desktop/file.txt"


file = open(directory, "r")
content = file.read()

answer = 5 + int(content)
print(answer)


