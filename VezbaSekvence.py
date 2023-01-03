name="Marko"

print(type(name))

print(name[2])

print(name[2:4])

rotiran_name=name[::-1]
print(rotiran_name)

print("Mar"*3)

a = ['H','l','o','W','r','d']
b = ['e','l',' ','o','l','']

for i in range(len(a)):
    print(a[i]+b[i],end="")
print()

print("New York".split())

print("apple#banana#orange".split('#'))

x = 1
print(eval('x+1'))

a = ['h','l','o','w','r','d']
b = ['e','l',' ','o','l','']
 
for i in range(len(a)):
    print("{}{}".format(a[i], b[i]), end = '')

groups = [['student1', 'student2', 'student3'],
 
    ['student4', 'student5', 'student6'],
 
    ['student7', 'student8', 'student9'],
 
    ['student10', 'student11', 'student12']]

groups.sort()
print(groups)

set_a = set(['a', 'b', 5, 2])
print("Set_a: {}".format(set_a))
 
set_b = {'a', 'c', 5, 4, None}
print("Set_b: {}".format(set_b))
 
 
print("Intersection: {}".format(set_a & set_b)) 
 
print("Union: {}".format(set_a | set_b)) 
 
print("Difference: {}".format(set_a - set_b))

lst=[1993, 1994, 1995, 1994, 1993, 1996] 
set_lst = set(lst) 
print(set_lst)

lst = list(set_lst) 
print(lst)

lst.sort() 
print(lst)

student_dict = {'Name':'Marco', 'Field':'Electrical engineering', 'Age':'20'}

values_dict = dict(first=1, second = 2)

cities_dict = {}
cities_dict['city1'] = 'New York'
cities_dict['city2'] = 'London'
cities_dict['city3'] = 'Moscow'

print(student_dict)
print(values_dict)
print(cities_dict)

England = {"capital": "London", "population": 8768000}
print(list(England.keys()))

capital = "London"
if len(capital) == 5:
    print(False)
else:
    print(True)

cities = ('Belgrade', 'Paris', 'Berlin', 'London')
print(len(cities))

cities = [['New York', 'London'], ['Paris', 'Berlin']]
cities[0].pop(1)
print(cities)

city1 = "LONDON";
city2 = "MOSCOW"
print(city1[-4:]+city2[-2:])

England = {"capital": "London", "population": 8768000}
print(England.get("capital"))

s="test"
print(s*3)

countries = {'UK':'London', 'DE':'Berlin', "FR":'Paris'}
list1 = []
for c in countries:
    list1.append(c)
print(list1)

list1 = [1,2,3]
list2 = [4,5,6]
print(max(list1+list2))

m_list = [['e1', 'e2'], ['London', 'Paris'], ['Susan', 'Maria']]
print[0][3]


