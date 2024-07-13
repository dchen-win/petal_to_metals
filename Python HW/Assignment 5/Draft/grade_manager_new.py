

class Student:
   
    def __init__(self, id, first_name, last_name): 
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.assignment = []
    # Method
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}" 

    assignments = []
    def get_assignments(self):
        # if f"{self.first_name} {self.last_name}" == name:
            return self.assignments
    
    def get_assignment(self, name):
        return self.assignments[0]
        # count = 0
        # for i in range (len(self.assignments)):
        #     count += 1
        #     if self.assignments[i] == name:
        #         print(count)
        #         return name
        #     else:
        #         print(count)
        #     return None

    # def get_average(self. *args):
    #     pass

    def submit_assignment(self, assignment):
        # insert() function inserts an element to the given index of an existing list
        self.assignments.insert(0, assignment)
        print("--------Submitted SUccessfully--------")

    def remove_assignment(self, name):
        if f"{self.first_name} {self.last_name}" == name:
            self.assignments.pop(0)
            print("-----------Removed Successfully-------")

    
class Assignments:

    def __init__(self, name, max_score):
        self.name = name
        self.max_score = max_score
        self.grade = None    # grade an integer representing the actual score on the assignment

#         Methods
    def assign_grade(self, grade):
        self.grade = grade  # sets the grade to the supplied integer grade value.
        if self.grade > self.max_score:
            self.grade = None 

    # def get_average(self):
    #     self.grade / self.max_score
     

std1 = Student(1, "smith", "jay")
std2 = Student(2, "john", "black")

fullname_of_std1 = std1.get_full_name()
fullname_of_std2 = std2.get_full_name()
print(f"Name: {fullname_of_std1}")
print(f"Name: {fullname_of_std2}")


assign1 = Assignments("Assign1 name", 10)   # Assignment 1
grade1= assign1.assign_grade(4)
print("Assignment 1 create: ", assign1)
print(assign1.grade)

assign2 = Assignments("Assign2 name", 10)   # Assignment 2
grade2= assign2.assign_grade(5)
print("Assignment 2 create: ", assign2)
print(assign2.grade)

assign3 = Assignments("Assign3 name", 10)   # Assignment 2
grade3= assign3.assign_grade(6)
print("Assignment 3 create: ", assign3)
print(assign3.grade)

# Submit the assignment
std1_assign1 = std1.submit_assignment(assign1)
std1_assign2 = std1.submit_assignment(assign2)
std1_assign3 = std1.submit_assignment(assign3)

std2_assign1 = std2.submit_assignment(assign1)
std2_assign2 = std2.submit_assignment(assign2)
std2_assign3 = std2.submit_assignment(assign3)


# Get all the assignment
print(f"List of all the assignments: {std1.get_assignments()}")
print(f"List of all the assignments: {std2.get_assignments()}")


# give the grade for student





#get the average
# print(std1.get_average())

# get assignment by name
print(f"Most recent assignment submitted by {fullname_of_std1} is: ", std1.get_assignment("name"))
print(f"Most recent assignment submitted by {fullname_of_std2} is: ", std2.get_assignment("name"))
# Remove assignment
std1.remove_assignment(fullname_of_std1)
print(std1.get_assignments())
std2.remove_assignment(fullname_of_std2)
print(std2.get_assignments())

