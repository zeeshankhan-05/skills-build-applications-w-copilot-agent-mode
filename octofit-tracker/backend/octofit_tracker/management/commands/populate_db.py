from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.conf import settings
from pymongo import MongoClient
from datetime import timedelta
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the database with test data for OctoFit tracker'

    def handle(self, *args, **kwargs):
        self.stdout.write('Creating test data...')

        # Create users
        users = [
            User.objects.create(_id=ObjectId(), username='coach_paul', email='paul.octo@mergington.edu', password='coachpass123'),
            User.objects.create(_id=ObjectId(), username='tech_jessica', email='jessica.cat@mergington.edu', password='techpass456'),
            User.objects.create(_id=ObjectId(), username='student_alex', email='alex.smith@mergington.edu', password='studentpass789'),
            User.objects.create(_id=ObjectId(), username='student_jordan', email='jordan.lee@mergington.edu', password='studentpass101'),
            User.objects.create(_id=ObjectId(), username='student_casey', email='casey.wong@mergington.edu', password='studentpass202')
        ]
        self.stdout.write('Users created successfully')

        # Create teams with members
        blue_team = Team.objects.create(
            _id=ObjectId(),
            name='Mergington Blue Dragons'
        )
        blue_team.members.add(users[0], users[2], users[4])  # Coach Paul and two students

        gold_team = Team.objects.create(
            _id=ObjectId(),
            name='Mergington Golden Eagles'
        )
        gold_team.members.add(users[1], users[3])  # Tech Jessica and one student
        self.stdout.write('Teams created successfully')

        # Create activities
        activities = [
            Activity.objects.create(
                _id=ObjectId(),
                user=users[2],
                activity_type='Running',
                duration=timedelta(minutes=45)
            ),
            Activity.objects.create(
                _id=ObjectId(),
                user=users[3],
                activity_type='Swimming',
                duration=timedelta(minutes=60)
            ),
            Activity.objects.create(
                _id=ObjectId(),
                user=users[4],
                activity_type='Basketball',
                duration=timedelta(minutes=90)
            ),
            Activity.objects.create(
                _id=ObjectId(),
                user=users[2],
                activity_type='Weightlifting',
                duration=timedelta(minutes=50)
            ),
            Activity.objects.create(
                _id=ObjectId(),
                user=users[3],
                activity_type='Soccer',
                duration=timedelta(minutes=75)
            )
        ]
        self.stdout.write('Activities created successfully')

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard.objects.create(
                _id=ObjectId(),
                user=users[2],
                score=95  # Alex
            ),
            Leaderboard.objects.create(
                _id=ObjectId(),
                user=users[3],
                score=88  # Jordan
            ),
            Leaderboard.objects.create(
                _id=ObjectId(),
                user=users[4],
                score=92  # Casey
            )
        ]
        self.stdout.write('Leaderboard entries created successfully')

        # Create workouts
        workouts = [
            Workout.objects.create(
                _id=ObjectId(),
                name='Morning Cardio',
                description='Start your day with an energizing cardio workout',
                difficulty_level='beginner'
            ),
            Workout.objects.create(
                _id=ObjectId(),
                name='Strength Basics',
                description='Fundamental strength training exercises',
                difficulty_level='beginner'
            ),
            Workout.objects.create(
                _id=ObjectId(),
                name='Team Sports',
                description='Group activities for team building',
                difficulty_level='intermediate'
            ),
            Workout.objects.create(
                _id=ObjectId(),
                name='Endurance Training',
                description='Build stamina and endurance',
                difficulty_level='advanced'
            ),
            Workout.objects.create(
                _id=ObjectId(),
                name='Flexibility Focus',
                description='Improve flexibility and reduce injury risk',
                difficulty_level='intermediate'
            )
        ]
        self.stdout.write('Workouts created successfully')

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with OctoFit test data!'))
