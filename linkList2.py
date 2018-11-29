"""
链表的创建

"""
class studentNode:
    def __init__(self,name='',cj=0,next = None):
        self._name = name
        self._cj = cj
        self._next = next
class student:
    def __init__(self):
        self._head = studentNode()
        self._dummpy = self._head
    def createStud(self,name,cj):
        newStud = studentNode(name,cj)
        self._dummpy._next = newStud
        self._dummpy = newStud
    def printStud(self):
        self._dummpy = self._head._next
        while self._dummpy != None:
            print(self._dummpy._name)
            self._dummpy = self._dummpy._next
    def findStud(self,cj):
        self._dummpy = self._head._next
        while (self._dummpy != None and self._dummpy._cj !=cj):
            self._dummpy = self._dummpy._next
        return self._dummpy
    def insertStud(self,studs,posStud):
        """ 在指定的位置插入元素
            studs是一个list对象，存放姓名和成绩
            posStud是在插入的位置对象
        """
        #posStud = self.findStud(studs[1])
        newStud = studentNode(studs[0],studs[1])
        #if posStud:
        newStud._next =posStud._next
        posStud._next = newStud
        #else:
         #   self._head._next = newStud

    def findPos(self,cj):
        self._dummpy = self._head._next
        if self._dummpy is None:  #空链表
            return self._head
        else:
            while(self._dummpy._next != None and self._dummpy._cj != cj):
                self._dummpy = self._dummpy._next
            return self._dummpy
            """
            while (self._dummpy._next != None):
                if self._dummpy._cj != cj:
                    self._dummpy = self._dummpy._next
                else:
                    return self._dummpy
            return self._dummpy
            """
#删除指定的成绩，删除链表
    def delStud(self,cj):
        self._dummpy = self._head
        while self._dummpy._next !=None and self._dummpy._next._cj !=cj:
            self._dummpy = self._dummpy._next
        if self._dummpy._next ==None and self._dummpy._cj != cj:
            return False
        else:
            self._dummpy._next = self._dummpy._next._next
            return True








stud = student()
"""
data = [['web',12],['pjzx',55],['ddd',65]]
for item in data:
    stud.createStud(item[0],item[1])
"""

rst = stud.findPos(65)
stud.insertStud(('fcl',88),rst)
rst = stud.findPos(88)
stud.insertStud(('pjzx',68),rst)
stud.printStud()
print('-'*50)
if stud.delStud(668):
    stud.printStud()
else:
    print('数据不存在')
"""
if rst:
    print(rst._name)
else:
    print("找不到")
"""

"""
head = student() #定义头结点
dummy = head
select = 0
num = 0
while select !=2:
    print("(1)新增 (2)离开 =>")
    try:
        select = int(input("请输入一个选项:"))
    except ValueError:
        print('输入错误')
        print('请重新输入\n')
    if select == 1:
        name = input("姓名:")
        age = int(input("年龄:"))
        sex = input("性别:")
        yuwen = int(input("语文"))
        shuxue = int(input("数学"))
        newStud = student(name,age,sex,yuwen,shuxue)
        dummy.next = newStud
        dummy = newStud
        num += 1
dummy = head.next
while dummy !=None:
    print(dummy._name)
    dummy = dummy.next
"""