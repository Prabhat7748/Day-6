# from distutils.log import error


a=int(input('enter no.: '))
b=int(input('enter other ni.: '))
try:
    print(a//b)
except:
    print("error")
else:
    print("got the result ")
finally:
    print('ok')
if b>0:
    raise ValueError


# raise
x=24
if x>20:
    raise Exception("number less than 20")