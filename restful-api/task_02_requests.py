#!/usr/bin/env python3
"""task_02_requests.py"""
import requests
import csv


def fetch_and_print_posts():
    """Fetch and print a post"""

    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    if response.status_code == 200:

        print("Status Code: 200")

        posts = response.json()

        for post in posts:
            print(post['title'])


def fetch_and_save_posts():
    """Fetch and save a post"""

    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:

        posts = response.json()

        with open('posts.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])

            writer.writeheader()

            for post in posts:
                writer.writerow({"id": post["id"], "title": post["title"], "body": post["body"]})
    else:
        print("Failed to fetch posts. Status code: {}".format(response.status_code))


fetch_and_print_posts()
fetch_and_save_posts()
