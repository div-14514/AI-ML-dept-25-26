# Emoji Mood Analyzer
positive = 0
negative = 0
mood_dict = {"love": 1, "happy": 1,"😍": 1,"great": 1,"good": 1,
             "hate": -1,"sad": -1,"😫": -1,"angry": -1,"bad": -1}


statement = input("Enter a sentence with words or emojis: ")

word=0
value=0


for word, value in mood_dict.items():
    if word in statement:
        if value == 1:
            positive += 1
        elif value == -1:
            negative += 1

# Compare counts and decide the mood
if positive > negative:
    print("Mood: Positive 😊")
elif negative > positive:
    print("Mood: Negative 😞")
else:
    print("Mood: Neutral 😐")
