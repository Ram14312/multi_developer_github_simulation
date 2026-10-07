from User import *
class Student(User):

    def __init__(self, user_id, name, age,enrolled_courses):
        super().__init__(user_id, name, age)
        self.enrolled_courses = enrolled_courses

    def show_details(self):
        studnet_detail = User.show_details()
        studnet_detail["enrolled_courses"] = self.enrolled_courses
        return studnet_detail