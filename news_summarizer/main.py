from ollama import chat
from ollama import ChatResponse
import feedparser

news_feeds = {
    "1": {
        "name": "BBC World News",
        "url": "http://feeds.bbci.co.uk/news/world/rss.xml"
    },
    "2": {
        "name": "CNN Top Stories (NOT IMPLEMENTED)",
        "url": "http://rss.cnn.com/rss/edition.rss"
    },
    "3": {
        "name": "Reuters World News (NOT IMPLEMENTED)",
        "url": "http://feeds.reuters.com/reuters/worldNews"
    },
    "4": {
        "name": "NBC News (NOT IMPLEMENTED)",
        "url": "https://www.nbcnews.com/id/3032091/device/rss/rss.xml"
    },
    "5": {
        "name": "CNBC News (NOT IMPLEMENTED)",
        "url": "https://www.cnbc.com/id/100727362/device/rss/rss.html"
    },
    "6": {
        "name": "ABC News (NOT IMPLEMENTED)",
        "url": "http://abcnews.go.com/abcnews/internationalheadlines"
    },
    "7": {
        "name": "Fox News",
        "url": "http://feeds.foxnews.com/foxnews/latest"
    },
}

debug = False

def fetch_news(feed_url):
    data = feedparser.parse(feed_url)
    return data

def summarize_news(news_list):
    response: ChatResponse = chat(model="llama3.2:1b", messages=[
        {
            "role": "user",
            "content": "Please summarize the news below and tell me what's happening recently. Format: [Title][Description]" + news_list,
        },
    ])
    return response["message"]["content"]

def main():
    while True:
        print("\nSelect a news source:")
        print("0. Exit")
        for key, feed in news_feeds.items():
            print(f"{key}.{feed["name"]}")

        choice = input("Enter your choice: ")
        if choice == '0':
            print("Exiting the program, bye!")
            break
        elif choice in news_feeds:
            feed = news_feeds[choice]
            print(f"Getting the latest news from {feed["name"]}\nPlease wait patiently!")
            data = fetch_news(feed["url"])
            print("Found", len(data.entries), "entries.")

            news_list = ""
            for entry in data.entries:
                news_list += f"{entry.title}\n{entry.summary}\n\n"

            if debug:
                print("Raw data:\n", data)

            summary = summarize_news(news_list)
            print(summary)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()