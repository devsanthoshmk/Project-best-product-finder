# Best product finder Python: product price comparison tool and e-commerce price tracker

A product price comparison tool and e-commerce price tracker that extracts catalog listings, prices, and reviews from online marketplaces and scores products using generative AI.

The best product finder Python scripts query Flipkart and Amazon to collect product pricing, customer feedback, and catalog metadata. The project parses HTML responses with XPath, retrieves API review records, and calculates product sentiment scores with Google Gemini.

## Architecture

The system consists of three modules:

1. Flipkart scraping engine
The scraper targets Flipkart search result and product review pages.
`flipkart scrapping/flipkart_scraper(final).py` prompts for a search query, formats the search URL, fetches HTML with browser headers, and parses grid (`_4ddWXP`) or list (`_2kHMtA`) containers. It extracts title, rating, price, and product URL for up to 20 items.
`flipkart scrapping/flipkart_scraper.py` reads product URLs, extracts individual review pages across 2 pages, collects rating scores, titles, and text, and saves rows into `delta.csv`.
`flipkart scrapping/final.py` runs a search query for laptops using list layout XPath selectors.
`flipkart scrapping/re for reviews.py` formats Flipkart product URLs into dedicated review endpoint paths.

2. Amazon API client
The client interfaces with RapidAPI endpoints for Amazon catalog data.
`amazon api/better than1(2) search.py` queries the Amazon Merchant Data search endpoint (`/search-products`) with query terms and country codes.
`amazon api/better than1(2) review.py` queries the Amazon Merchant Data review endpoint (`/get-reviews`) using product ASINs.

3. AI opinion evaluation and utilities
The evaluation module generates automated product assessments.
`flipkart scrapping/chat gpt api.py` sends product review prompts to Google Gemini Pro (`gemini-pro`) to produce an opinion summary and a score out of 5.
`flipkart scrapping/re for getting ai score.py` parses the numerical opinion score from Gemini text output with a regular expression pattern.
`multithreading1.py` tests thread creation for parallel execution using Python `threading.Thread`.

## Setup

1. Clone the repository:
```bash
git clone https://github.com/devsanthoshmk/Project-best-product-finder.git
cd Project-best-product-finder
```

2. Install required Python packages:
```bash
pip install requests lxml google-generativeai ipython
```

3. Ensure Python 3.8 or higher is installed.

## Usage

1. Scrape Flipkart search results:
```bash
python3 "flipkart scrapping/flipkart_scraper(final).py"
```
The script prompts for a search query, queries Flipkart, and prints extracted products with titles, ratings, prices, and links.

2. Scrape Flipkart products with reviews to CSV:
```bash
python3 "flipkart scrapping/flipkart_scraper.py"
```
The script scrapes search listings, fetches up to 2 review pages per product, and writes structured records to `delta.csv`.

3. Search Amazon products via RapidAPI:
```bash
python3 "amazon api/better than1(2) search.py"
```

4. Fetch Amazon reviews by ASIN via RapidAPI:
```bash
python3 "amazon api/better than1(2) review.py"
```

5. Generate AI opinion scores:
```bash
python3 "flipkart scrapping/chat gpt api.py"
```
The script calls Gemini Pro to summarize reviews and produce an opinion score.

6. Extract numerical scores from AI text:
```bash
python3 "flipkart scrapping/re for getting ai score.py"
```

## Configuration

The scripts use the following configuration parameters:

1. RapidAPI headers
Edit `amazon api/better than1(2) search.py` and `amazon api/better than1(2) review.py` to specify your RapidAPI credentials:
- `X-RapidAPI-Key`: Your RapidAPI subscription key.
- `X-RapidAPI-Host`: `amazon-merchant-data.p.rapidapi.com`.

2. Google Gemini API key
Set your Gemini API key in `flipkart scrapping/chat gpt api.py`:
- `genai.configure(api_key="YOUR_GEMINI_API_KEY")`

3. Request headers
Flipkart scrapers define custom User-Agent strings in `headers` dictionaries to simulate desktop browser requests.

4. Result limits
Search scrapers cap output at 20 products per query using list slicing `[:20]`. Review scrapers iterate over 2 review pages per product.
