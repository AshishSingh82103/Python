# File handling

file = open('youtube.txt', 'w')

try:
    file.write('chai ur code')
finally:
    file.close()

#Other way and final way

with open('youtbe.txt', 'w') as file:
    file.write('chai ur code')
    