marks = []
total = 0
print("enter marks obtained in 5 subjects:")
for i in range(5):
    marks.insert(i,int(input()))
for i in range(5):
    total=total + marks[i]
avg=total/5
perc=(total/500)*100
print(end="avg percentage of marks =")
print(perc)
