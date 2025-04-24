from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import User, Team, Activity, Leaderboard, Workout

class OctoFitTests(APITestCase):
    def setUp(self):
        # Create test user
        self.user = User.objects.create(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        
        # Create test team
        self.team = Team.objects.create(
            name='Test Team'
        )
        
        # Create test workout
        self.workout = Workout.objects.create(
            name='Test Workout',
            description='Test workout description',
            difficulty_level='beginner'
        )

    def test_create_user(self):
        url = reverse('user-list')
        data = {'username': 'newuser', 'email': 'new@example.com', 'password': 'newpass123'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)

    def test_create_activity(self):
        url = reverse('activity-list')
        data = {
            'user': self.user.id,
            'activity_type': 'running',
            'duration': '00:30:00'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_leaderboard(self):
        url = reverse('leaderboard-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
