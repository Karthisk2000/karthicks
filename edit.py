file = open('karthi')
print(file.readline())
print(file.read())
file.close()

with open('karthi','r') as reader:
    content = reader.readline()#[abc,sfsdf,cat,dog,line]
    sort(content)#[line,dog,cat,sfsdf,abc]
    with open('karthi','w') as writer:# reversed
        for line in sort(content):
            writer.write(line)