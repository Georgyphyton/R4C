from django.test import TestCase, Client
from robots.models import Robot
from django.urls import reverse_lazy
import json
# Create your tests here.


class TestRobots(TestCase):

    def setUp(self):
        self.client = Client()
        self.post_robot_url = reverse_lazy('add_robot')
        self.test_robot = {"model": "11", "version": "22", "created": "2023-10-03 23:59:59"}
        self.json_test_robot = json.dumps(self.test_robot)
        self.wrong_test_robot = json.dumps({"model": "11", "version": "223", "created": "2023-10-03 23:59:59"})

    def test_post_robot(self):
        response = self.client.post(self.post_robot_url, self.json_test_robot, content_type="application/json")
        self.assertEqual(response.status_code, 201)
        self.robot = Robot.objects.get(pk=1)
        self.assertEqual(self.robot.version, self.test_robot['version'])
        self.assertIn(b'New robot has been created with id 1', response.content)

    def test_wrong_post(self):
        response = self.client.post(self.post_robot_url, self.wrong_test_robot, content_type="application/json")
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Incorrect data entry format!', response.content)
        self.assertEqual(Robot.objects.count(), 0)
