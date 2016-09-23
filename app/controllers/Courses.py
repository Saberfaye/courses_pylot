from __future__ import print_function
from system.core.controller import *
import sys
# print (friends, file=sys.stderr)

class Courses(Controller):
    def __init__(self, action):
        super(Courses, self).__init__(action)
        self.load_model("CourseModel")
        self.db = self._app.db
   
    def index(self):
        courses = self.models["CourseModel"].get_courses()
        return self.load_view("index.html", all_courses = courses)

    def add(self):
        post = request.form
        add_status = self.models["CourseModel"].add_course(post)
        if add_status["status"] == False:
            for message in add_status["errors"]:
                flash(message, "name")
        return redirect("/")

    def destroy(self, id):
        course = self.models["CourseModel"].get_course(id)[0]
        return self.load_view("destroy.html", course = course)

    def delete(self, id):
        self.models["CourseModel"].delete_course(id)
        return redirect("/")


