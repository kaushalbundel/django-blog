from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Post
from datetime import datetime

# Create your tests here.


class BlogTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser", email="test@test.com", password="secret"
        )
        self.post = Post.objects.create(
            title="A good title", body="Nice body content", author=self.user
        )

    def test_string_representation(self):
        post = Post.objects.create(
            title="A Good Title",
            body="Nice Body Content",
            author=self.user,
            created_date=datetime.now().strftime("%Y-%m-%d, %H:%M:%S"),
        )
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(f"(self.post.title)", "A good title")
        self.assertEqual(f"(self.post.author)", "testuser")
        self.assertEqual(f"(self.post.body)", "Nice Body Content")

    def test_post_list_view(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response, "Nice Body Content")
        self.assertTemplateUsed(response, "home.html")

    def test_post_detail_view(self):
        response = self.client.get("post/1/")
        no_response = self.client.get("post/1000/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "A good title")
        self.assertTemplateUsed(response, "detail.html")

    def test_get_absolute_url(self):
        self.assertEqual(self.post.get_absolute_url(), "/post/1/")
