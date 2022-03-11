var = 'm'

try:
    num = int(var)
    print(num)
except Exception as e:
    print(type(e))
    print('something bad happened')
else:
    print('nothing bad happened')
finally:
    print("something bad either happened or it didn't")