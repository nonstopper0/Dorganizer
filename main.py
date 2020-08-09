
try:
    open('Data.txt', 'r')
except: 
    newFile = open('Data.txt', 'w+')
    for i in range(5):
        text = f'This is line {i + 1} of 5\n'
        newFile.write(text)

    newFile.close()

saveFile = open('Data.txt', 'r+')

text = saveFile.read

print(text)