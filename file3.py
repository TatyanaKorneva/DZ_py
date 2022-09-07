x=int(input())
y=int(input())
if x>0 and y>0:
    print('I четверть')
elif x>0 and y<0:
    print('IV четверть')
elif x<0 and y<0:
    print('III четверть')
elif x<0 and y>0:
    print('II четверть')
else:
    print('Точка лежит на оси')
