with open('/Users/saulenko/Documents/Python/Example.txt', 'r') as example:
    #file_stuff=example.read()
    file_lines=example.readlines()
    #print(file_stuff)
    print(file_lines[1])
    #file_lines=example.readline()
    #print(file_lines)
    print(example.name)

    #for line in example:
    #    print(line)
#print(example.closed)
#print(file_stuff)



print(type(file_lines))
