# Automated Bot

Object of this bot demonstrate functionalities of the system according to defined rules. This bot
reads rules from a config json file.

Bot creates this activity:

● signup users (number provided in config)

● each user creates random number of posts with integer content (up to max_posts_per_user)

● After creating the signup and posting activity, posts are liked randomly, posts
can be liked multiple times

## Usage

```python
python main.py
```
