# Chat with website

Given a website URL, scrape it, and enable chatting with its contents.

An MVP for the solution can be:

1. Just one page scraped (no crawling)
2. Possible to ask questions about text contents and get reasonable answers

It should work with large volumes of text, well past LLM context window limits.

This is an open-ended problem, e.g. any UI to interact/"chat" with the data is acceptable.

Direction ideas:

- Accept a URL input and start talking to contents on that URL (as opposed to hardcoded single URL)
- Web-based chat UI
- Persisted data: after a URL is scraped once, it doesn't need to be re-scraped
- Scrape entire website: follow links recursively (to some depth) starting from a root/base URL
- Allow talking with data from several websites at once (with an aggregate of the contents)
- Allow speaking with the data by voice, instead of by chat
- Allow querying the structure/sitemap, not just contents (e.g. "how many pages are there?", "what external links are there?")
- Allow issuing commands/interacting with the URL, not just scraping and querying
- Support content types beyond text: images, data/JSON (e.g. for API request URLs; could e.g. provide additional context about what the data is in addition to the URL to get better results)
- (feel free to implement your own ideas as well)

The solution should include at least 1-2 features beyond the barebones MVP.

## Advice

- Use off-the-shelf solutions when possible (e.g. scraping/extracting text from HTML)
- Get minimal end-to-end prototype working before adding extra features
