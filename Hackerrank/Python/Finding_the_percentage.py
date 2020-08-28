n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
x=student_marks[input()]
print("{0:.2f}".format(sum(x)/len(x)))

