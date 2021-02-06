from ExcerciseUdemyYoutube.YoutubeCodeExercise.Class_exercise import Student

# this exercise shows how to create object of students and get their nattributes after
student_Daniel = Student("Daniel", 8.5, "Virsuliskes")
student_Vilte = Student("Vilte", 10, "Justiniskes")

List_of_students = [student_Daniel, student_Vilte]

for students in List_of_students:
    print(students.name)
