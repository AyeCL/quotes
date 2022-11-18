import requests
import sys

def get_tags():     # Call using "quote ls tags"
    url = requests.get('https://api.quotable.io/tags')
    tags = url.json()
    # Print the names of tags
    for tag in tags:
        print(tag["name"])

def get_authors():      # Call using "quote ls authors"
    url = requests.get('https://api.quotable.io/authors')
    authors = url.json()
    # Print the names of authors
    for author in authors["results"]:
        print(author["name"])

def get_random_quote():     # Call using "quote random"
    url = requests.get('https://api.quotable.io/random')
    quote = url.json()
    print("\"", quote["content"], "\"", sep="")
    print("-", quote["author"])

def get_quote_by_tag(tag):  # Call using "quote tag <tag>"
    url = requests.get('https://api.quotable.io/random?tags=' + tag)
    quote = url.json()
    print("\"", quote["content"], "\"", sep="")
    print("-", quote["author"])

def get_quote_by_author(author):    # Call using "quote author <author>"
    url = requests.get('https://api.quotable.io/search/authors?query=' + author)
    quote = url.json()
    # Print the bio of the author
    print(quote["results"][0]["bio"])
    print()
    # Print a random quote by the author
    authorSlug = quote["results"][0]["slug"]
    url = requests.get('https://api.quotable.io/random?author=' + authorSlug)
    quote = url.json()
    print("\"", quote["content"], "\"", sep="")
    print("-", quote["author"])


def get_quote_search(search):   # Call using "quote search <search>"
    url = requests.get('https://api.quotable.io/search/quotes?query=' + search)
    quote = url.json()
    # Get the number of results
    numResults = quote["count"]
    # Print the number of results
    print("Found", numResults, "results.")
    if numResults > 0:
        if numResults < 5:
            numResults = numResults
        else:
            numResults = 5
            print("Showing first 5 results.\n")
        # Print the first 5 results
        for i in range(numResults):
            print("\"", quote["results"][i]["content"], "\"", sep="")
            print("-", quote["results"][i]["author"])
            print()

def main():
    if len(sys.argv) == 1:
        get_random_quote()
    elif sys.argv[1] == "ls":
        if len(sys.argv) == 2:
            # Print both tags and authors
            print("Tags:\n")
            get_tags()
            print("\n\nAuthors:\n")
            get_authors()
        elif sys.argv[2] == "tags":
            get_tags()
        elif sys.argv[2] == "authors":
            get_authors()
        else:
            print("Usage: quote ls <tags|authors>")
    elif sys.argv[1] == "random":
        get_random_quote()
    elif sys.argv[1] == "tag":
        get_quote_by_tag(sys.argv[2])
    elif sys.argv[1] == "author":
        get_quote_by_author(sys.argv[2])
    elif sys.argv[1] == "search":
        get_quote_search(sys.argv[2])
    elif sys.argv[1] == "help":
        print("Usage: quote OR quote <command> [options]")
        print("Commands:")
        print("  ls tags\t\tList all tags")
        print("  ls authors\t\tList all authors")
        print("  random\t\tGet a random quote")
        print("  tag <tag>\t\tGet a random quote by tag")
        print("  author <author-name>\tGet a bio of an author and a random quote by them")
        print("  search <search-term>\tSearch for a quote")
        print("  help\t\t\tShow this help message")
    else:
        print("Usage: quote OR quote <command> [options]")
        print("Commands:")
        print("  ls tags\t\tList all tags")
        print("  ls authors\t\tList all authors")
        print("  random\t\tGet a random quote")
        print("  tag <tag>\t\tGet a random quote by tag")
        print("  author <author-name>\tGet a bio of an author and a random quote by them")
        print("  search <search-term>\tSearch for a quote")
        print("  help\t\t\tShow this help message")

if __name__ == "__main__":
    main()
