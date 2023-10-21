import json
import random

# Path to the config file
CONFIG_FILE = "config.json"


def create_users(num_users: int) -> list:
    return [f"User{i}" for i in range(1, num_users + 1)]


def create_posts(users: list, max_posts_per_user: int) -> list:
    posts = []
    for user in users:
        num_posts = random.randint(1, max_posts_per_user)
        # Create and add posts to the list
        for i in range(num_posts):
            post = {
                "user": user,
                "content": random.randint(100, 1000)
            }
            posts.append(post)
    return posts


def random_likes(users: list, posts: list, max_likes_per_user: int) -> None:
    user_likes = {user: set() for user in users}

    for user in users:
        num_likes = random.randint(1, max_likes_per_user)
        liked_posts = random.sample(posts, num_likes)
        for post in liked_posts:
            # Like post only if the user hasn't liked the same post already
            if post["content"] not in user_likes[user]:
                user_likes[user].add(post["content"])
                print(f"{user} liked post by {post['user']}: {post['content']}")


def main(config_file: str) -> None:
    # Open the config file and catch the errors if there are any
    try:
        with open(config_file, "r") as f:
            config = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error: {e}")
        return

    # Declare rules from config file
    number_of_users = config["number_of_users"]
    max_posts_per_user = config["max_posts_per_user"]
    max_likes_per_user = config["max_likes_per_user"]

    users = create_users(number_of_users)  # Create list of users
    posts = create_posts(users, max_posts_per_user)  # Create random posts and add to the list
    random_likes(users, posts, max_likes_per_user)  # Like random post


if __name__ == "__main__":
    main(CONFIG_FILE)
