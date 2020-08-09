global file

try:
    file = open('Data.txt', 'r+')

except: 
    file = open('Data.txt', 'w')
    file.write(data)

finally: 
    print('done')
    file.close()
