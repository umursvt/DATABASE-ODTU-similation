import sqlite3
class University():
    def __init__(self,name,university):
        self.name = name
        self.university = university
        self.status =True
        self.connect()

    def run(self):
        self.menu()
        self.status =True

        choice = self.choice()

        if choice == 1:
            self.addStudent()
        elif choice == 2:
            self.deleteStudent()
        elif choice == 3:
            pass
        elif choice == 4:
            pass
        elif choice == 5:
            pass

    def menu(self):
        print("*********** {}  Administration System ***********".format(self.name))
        print(""""\n
        1) Add Student\n
        2) Delete Student\n
        3) Update Student\n
        4)Show All Student\n
        5)Exit\n
        """)

    def choice(self):
        while True:
            try:
                progress = int(input("Select:"))
                if progress<1 or progress>6:
                    print("Operation number must be between 1-6")
                    continue
                break
            except ValueError:
                print("Operation must be an integer. Please write correct type of input.")
        return  progress


    def addStudent(self):
        print("Student İnformations")
        name = input("Student name: ").lower().capitalize()
        surname = input("Student surname: ").lower().capitalize()
        faculity = input("Student faculity: ").lower().capitalize()
        department = input("Student department: ").lower().capitalize()
        stu_ID = input("Student ID: ")


        while True:
            try:
                typ= int(input("Student's Education Type: "))
                if typ <1 or typ >3:
                    print("IT MUST BE 1 OR 2")
                    continue
                break
            except:
                print("It is not suitable form. only integers")
        status ="active"

        self.cursor.execute("INSERT INTO students VALUES('{}','{}','{}','{}','{}',{},'{}')".format(name,surname,department,faculity,stu_ID,typ,status))
        self.connect.commit()
        print("Sudent named {} {} added succesfuully".format(name,surname))

    def deleteStudent(self):
            self.cursor.execute("SELECT * FROM students")

            allStudent = self.cursor.fetchall()

            converstr = lambda x: [str(y) for y in x]

            for i, j in enumerate(allStudent, 1):
                print("{}){}".format(i, " ".join(converstr(j))))
            while True:
                try:
                    select = int(input("Select the student to be deleted"))
                    break
                except ValueError:
                    print("incorrect")

            self.cursor.execute("DELETE FROM students WHERE rowid={}".format(select))
            self.connect.commit()
            print("STUDENT DELETED SUCCESFULLY")





    def updateStudent(self):
        self.cursor.execute("SELECT * FROM students")

        allStudent = self.cursor.fetchall()

        converstr = lambda x: [str(y) for y in x]

        for i, j in enumerate(allStudent, 1):
            print("{}){}".format(i, " ".join(converstr(j))))
        while True:
            try:
                select = int(input("Select the student to be deleted"))
                break
            except ValueError:
                print("incorrect")

       





    def showAllStudents(self,by):
        pass

    def systemExit(self):
        self.status = False


    def connect(self):
        self.connect = sqlite3.connect("ODTU.db")
        self.cursor = self.connect.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS students(name TEXT, surname TEXT,faculity TEXT,department TEXT,studentID INT,type INT,status TEXT)")
        self.connect.commit()





ODTU = University("ODTU","Türkiye")

while ODTU.status:
    ODTU.run()