with open('karthi','r') as reader:
    content = reader.readline()#[abc,sfsdf,cat,dog,line]
    reversed(content)#[abc,sfsdf,cat,dog,line]
    with open('karthi','w') as writer:
        for line in reversed(content):
            writer.write(line)