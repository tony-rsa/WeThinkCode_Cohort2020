import random

def create_outline():
    """
    TODO: implement your code here
    """
    problems = dict()
    problem_list = ["Problem 1", "Problem 2", "Problem 3"]
    topics_list = ["Introduction to Python", "Tools of the Trade", 
                  "How to make decisions", "How to repeat code",\
                   "How to structure data", "Functions", 
                  "Modules"]
    topics_list.sort()
    course_topics = set(topics_list)
    
    #step 1
    print("Course Topics:")
    for topics in sorted(course_topics):    
        print("* "+topics)
        #populating map for step 2
        problems[topics] = problem_list

    #step 2
    print("Problems:")
    for problem in course_topics:
        #printing map headings
        print("* "+problem+" : ", end="")
        for x in range(0, 3):
            #printing map problems
            print(problems[problem][x], end="")
            #adding commas
            if x < 2:
                print(", ", end="")
        print()

    #step 3
    student_progress = [""]
    student_tuple_data = ()
    status = ["[STARTED]","[GRADED]","[COMPLETED]"]
    name_list = ["Bob", "Adam", "Eve"]
    for x in range(0, 3):
        student_tuple_data += (name_list[x],)
        student_tuple_data += (topics_list[random.randint(0, 6)],)
        student_tuple_data += (problem_list[random.randint(0, 2)],)
        student_tuple_data += (status[x],)
    student_progress = list(student_tuple_data)

    #printing
    print("Student Progress:")
    y = 0
    z = 0
    while y < 3:
        print("{}. ".format(y+1), end="")
        print(student_progress[z], end=" - ")
        print(student_progress[z+1], end=" - ")
        print(student_progress[z+2], end=" ")
        print(student_progress[z+3])
        y += 1
        z += 4


if __name__ == "__main__":
    create_outline()
