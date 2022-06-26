def numbers(students):
    subject=[]
    num={}

    num_std=len(students)
    for n in range(num_std):
        for e in students[n]:
            if not e in subject:
                subject.append(e)


    for s in subject:
        c=0
        for n in range(num_std):
            if s in students[n]:
                c=c+1
        num.update({s:c})
    return(num)
print("number of students")
n=int(input())
students=[]
li=[]
for i in range(n):
    print("enter no. of subjects for student",(i+1))
    st=int(input())
    print("enter the subjects")
    li=[]
    for j in range(st):
        ele=input()
        li.append(ele)
    students.append(li)
print(students)
num=numbers(students)
def popular(num):
    mx=0
    de=len(num)
    for key,value in num.items():
        if value>mx:
            mx=value
            popular_course=key
    print("most popular course=")
    return(popular_course)
print(popular(num))