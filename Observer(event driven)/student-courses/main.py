from course import Course
from student import Student

s1 = Student("ahmed")
s2 = Student("moahmed")
s3 = Student("noha")

c1 = Course("db")
c2 = Course("c++")

c1.subscribe(s1)
c1.subscribe(s2)
c1.subscribe(s3)

c2.subscribe(s2)
c2.subscribe(s3)

# here we set the availability of db course to available
c1.setavailability(1)
# notify all student(observers) that subscribe to that course
c1.notifyallsubscribers()
