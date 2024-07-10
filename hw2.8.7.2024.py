score: int = int(input("Please enter the test score: "));
if score < 0 or score > 100:
    print("grade illegal");
elif score <= 40:
    print("try harder next time");
elif score <= 60:
    print("you're getting there, need some more work");
elif score <= 80:
    print("pretty good");
elif score <= 95:
    print("awesome!");
elif score <= 100:
    print("excellent! You're a Star");
