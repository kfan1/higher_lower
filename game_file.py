import random
import art
import followers


def game(score):
    a = random.choice(followers.data)
    b = random.choice(followers.data)
    print(f"Compare A: {a['name']}, a {a['description']} from {a['country']}")
    print(art.vs)
    print(f"Against B: {b['name']}, a {b['description']} from {b['country']}")
    guess = input("Who has more instagram followers? A or B: ").lower()
    if a['follower_count'] > b['follower_count']:
        answer = "a"
    else:
        answer = "b"
    if guess == answer:
        score += 1
        print("\n" * 25)
        print(art.logo)
        print(f"You're right! {a['name']} has {a['follower_count']} million followers, {b['name']} has {b['follower_count']} million. Current score: {score}")
        game(score)
    else:
        print(f"\nYou're wrong. {a['name']} has {a['follower_count']} million followers, {b['name']} has {b['follower_count']} million. Final score: {score}")
        return
