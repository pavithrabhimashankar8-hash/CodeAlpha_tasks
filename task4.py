from textblob import TextBlob

print("=" * 60)
print("      CODEALPHA DATA ANALYTICS - TASK 4")
print("           SENTIMENT ANALYSIS")
print("=" * 60)

while True:

    text = input("\nEnter a sentence (or type 'exit' to quit): ")

    if text.lower() == "exit":
        print("\nThank You!")
        break

    analysis = TextBlob(text)

    polarity = analysis.sentiment.polarity

    print("\nPolarity Score :", polarity)

    if polarity > 0:
        print("Sentiment : Positive 😊")

    elif polarity < 0:
        print("Sentiment : Negative 😔")

    else:
        print("Sentiment : Neutral 😐")

print("\nProject Completed Successfully")
print("=" * 60)