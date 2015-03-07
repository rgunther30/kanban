from django.test import TestCase, Client
from board.models import Task, AddTaskForm
from django.contrib.auth.models import User
from django.utils import timezone

class TaskInitTestCase(TestCase):
	time = timezone.now() 
	def setUp(self):
		User.objects.create(
			username = "TestUser",
			first_name = "Test",
			last_name = "User",
			email = "test@email.com",
			password = "pbkdf2_sha256$15000$NyuMeIREUpFM$IJzDldsB/KVcQiH3sYCfPIREA9q2UdEVQ3GlYEEDbVk="
			)

		user = User.objects.get(username="TestUser")

		Task.objects.create(
		    creator = user,
		    owner = user,
		    creation_date = self.time,
		    description = "Test Object.",
		    name = "Test Name",
		    state = "To do"
			)

	def test_task_exists(self):
		user = User.objects.get(username="TestUser")
		t = Task.objects.get(name="Test Name")
		self.assertEqual(t.creator, user)
		self.assertEqual(t.owner, user)
		#self.assertEqual(t.creation_date, self.time)
		self.assertEqual(t.state, "To do")

	def test_login_logout(self):
		c = Client()
		u = User.objects.get(username="TestUser")
		u.set_password('test123')
		u.save()
		response = c.login(username="TestUser", password="test123")
		self.assertEqual(response, True)
		reponse = c.logout()
		self.assertEqual(response, True)

	def test_board_pages(self):
		c = Client(HTTP_USER_AGENT='Mozilla/5.0')
		response = c.get('/board/', follow=True)
		self.assertEqual(response.status_code, 200)
		response = c.get('/board/add/', follow=True)
		self.assertEqual(response.status_code, 200)
		response = c.get('/board/edit/', follow=True)
		self.assertEqual(response.status_code, 200)
		response = c.get('/board/login', follow=True)
		self.assertEqual(response.status_code, 200)
		response = c.get('/board/logout', follow=True)
		self.assertEqual(response.status_code, 200)
		response = c.get('/board/profile', follow=True)
		self.assertEqual(response.status_code, 200)		
		response = c.get('/board/about', follow=True)
		self.assertEqual(response.status_code, 200)		

	def test_adding_task(self):
		c = Client(HTTP_USER_AGENT='Mozilla/5.0')
		form = AddTaskForm(
			{'creator': '1', 
			'owner': '1', 
			'description': 'Test task', 
			'name':'Test', 
			'state':'To do'})
		self.assertTrue(form.is_valid())

		saved_form = form.save()
		test_task = Task.objects.get(name='Test')
		self.assertTrue(test_task.owner, 'TestUser')
		self.assertTrue(test_task.creator, 'TestUser')
		self.assertTrue(test_task.description, 'Test task')
		self.assertTrue(test_task.name, 'Test')
		self.assertTrue(test_task.state, 'To do')

	def test_change_state(self):
		test_task = Task.objects.get(name='Test Name')
		self.assertTrue(test_task.state, "To do")	
		test_task.state = "In Progress"
		self.assertTrue(test_task.state, "In Progress")
		test_task.state = "Finished"
		self.assertTrue(test_task.state, "Finished")		

if '__main__' == __name__:
	unittest.main()
