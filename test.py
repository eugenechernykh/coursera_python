def tranform(myStr):

    return myStr.split()

myStr = 'aaaaa bbbb'
#print(' '.join(map(str, map(lambda myStr: tuple(myStr.split(' ')), myStr))))
print(tranform(myStr))
print(' '.join(map(str, (map(lambda myStr: myStr.split(), myStr)))))