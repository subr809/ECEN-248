with open('Transcript.txt', 'w+') as grades:
    print("Welcome to the Grade Calculator! This program can calculate your final grade for a class "
          "and/or give you the exact grade you need on the final exam to make a certain grade in a class.")
    numofclasses = int(input("How many classes do you want to calculate your grade for? : "))
    for i in range(numofclasses):
        final = []
        course = input("Please enter a course: ")
        grades.write(course + '\n')
        grades.write(("{0:<20}{1:^20}{2:^20}".format("Category", "Percentage of Grade", "Points Earned"))+'\n')
        categories = int(input("How many grading categories would you like to add?(Exams, assignments, quizzes, etc.): "))
        percentages = []
        for x in range(categories):
            pachieved = []
            ppossible = []
            achieved = 0
            possible = 0
            category = input("Enter a grading category: ")
            percentage = float(input("Enter the weight of this category:(Ex: 20) "))
            percentages.append(percentage)
            gradestyle = input("To calculate the total grade, choose whether to enter every "
                                   "assignment in this category or the total points for this category. "
                                   "Enter 'A' to choose each assignment. Enter 'B' to choose total points: ")
            gradestyle = gradestyle.strip().capitalize()
            if gradestyle == 'A':
                while achieved != -1:
                    achieved = float(input("Enter the points earned on the assignment. When you finish "
                                               "entering every assignment, type '-1': "))
                    if achieved == -1:
                        break
                    pachieved.append(achieved)
                    possible = float(input("Enter the points possible on this assignment: "))
                    ppossible.append(possible)
            else:
                achieved = float(input("Enter the total number of points achieved in this category: "))
                possible = float(input("Enter the total number of points possible in this category: "))
                pachieved.append(achieved)
                ppossible.append(possible)
            pachieved = sum(pachieved)
            ppossible = sum(ppossible)
            total = round((pachieved / ppossible) * percentage, 2)
            final.append(total)
            grades.write(("{0:<20}{1:^20}{2:^20}".format(category, percentage, total)) + '\n')
        final = (sum(final))
        grades.write("\n" + "Grade: " + str(final) + '/' + str(sum(percentages)) + '\n\n')
# Figuring out what you need on the final to make a certain grade in the class.
        if sum(percentages) != 100.0:
            question = input("Enter 'Yes' if you would like to calculate the grade needed on the final exam to "
                                 "achieve a certain grade. If not, enter any other key: ")
            question = question.strip().capitalize()
            if question == 'Yes':
                A = float(input("What is the numerical equivalent to an A in this class?: "))
                B = float(input("What is the numerical equivalent to a B in this class?: "))
                C = float(input("What is the numerical equivalent to a C in this class?: "))
                D = float(input("What is the numerical equivalent to a D in this class?: "))
                finalexam = float(input("What percentage of the final grade does the final exam account for? "))
                if final >= A:
                    grades.write("You already have at least an A in this class." + '\n')
                else:
                    grades.write("The grade you need to make on the final for an A in this class is a " + str(
                        round((((A - final) / finalexam) * 100), 2))+ '\n')
                if final >= B:
                    grades.write("You already have at least a B in this class." + '\n')
                else:
                    grades.write("The grade you need to make on the final for a B in this class is a " + str(
                        round((((B - final) / finalexam) * 100), 2)) + '\n')
                if final >= C:
                    grades.write("You already have at least a C in this class." + '\n')
                else:
                    grades.write("The grade you need to make on the final for a C in this class is a " + str(
                        round((((C - final) / finalexam) * 100), 2)) + '\n')
                if final >= D:
                    grades.write("You already have at least a D in this class." + '\n')
                else:
                    grades.write("The grade you need to make on the final for a D in this class is a " + str(
                        round((((D - final) / finalexam) * 100), 2)) + '\n')
            else:
                continue
        grades.write('----------------------------------------------------------------------' + '\n')