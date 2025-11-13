import wikipedia

search_topic = "Python (programming language)"

summary = wikipedia.summary(search_topic)

print(f"📘 Summary for: {search_topic}\n")
print(summary)
