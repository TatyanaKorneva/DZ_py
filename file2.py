x=int(input())
y=int(input())
z=int(input())
assert (x==0 or x==1) and (y==0 or y==1) and (z==0 or z==1), 'Введено недопустимое значение'
left = not (x or y or z)
right = not x and not y and not z
result = left == right
print(result)