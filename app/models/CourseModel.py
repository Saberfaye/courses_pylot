from system.core.model import Model

class CourseModel(Model):
	def __init__(self):
		super(CourseModel, self).__init__()

	def get_courses(self):
		query = "SELECT * from courses ORDER BY created_at DESC"
		return self.db.query_db(query)

	def get_course(self, course_id):
		query = "SELECT * from courses where id = :id"
		data = {'id': course_id}
		return self.db.query_db(query, data)

	def add_course(self, course):
		errors = []
		if not course['name']:
			errors.append('Course name cannot be blank')
		elif len(course['name']) < 15:
			errors.append('Course name must be at least 15 characters long')

		if errors:
			return {"status": False, "errors": errors}
		else:
			query = "INSERT into courses (name, description, created_at) VALUES(:name, :description, NOW())"
			data = {'name': course['name'], 'description': course['description']}
			self.db.query_db(query, data)
			return { "status": True }

	def delete_course(self, course_id):
		query = "DELETE FROM courses WHERE id = :course_id"
		data = { "course_id": course_id }
		return self.db.query_db(query, data)
