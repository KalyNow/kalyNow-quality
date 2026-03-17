"""
locustfile.py

Main Locust entry point for KalyNow API load tests.

Defines user behaviors by composing high-level scenario flows.
Each @task method simulates one realistic user interaction.

Usage:
    locust -f load-tests/locustfile.py --host=http://localhost:8000
"""

from locust import HttpUser, between, task

from scenarios.user_signup_flow import signup_and_login
from scenarios.create_offer_flow import create_restaurant_and_offer


class KalyNowUser(HttpUser):
    """
    Simulates a standard KalyNow user performing common actions.

    wait_time: random pause between 1 and 3 seconds between tasks,
               mimicking real user think time.
    """

    wait_time = between(1, 3)

    def on_start(self):
        """Called once when a simulated user starts. Perform login here."""
        self.auth_token = signup_and_login(self.client)

    @task(3)
    def browse_and_create_offer(self):
        """
        High-frequency task: create a restaurant and an offer.
        Weight 3 means this runs 3x more often than weight-1 tasks.
        """
        create_restaurant_and_offer(self.client, self.auth_token)

    @task(1)
    def signup_flow(self):
        """Low-frequency task: simulate a new user signing up."""
        signup_and_login(self.client)
