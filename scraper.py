import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

# The Code below is for fetching the BBC News homepage
url = "https://www.bbc.com/news"
response = requests.get(url)  # This line sends HTTP request to BBC
# This line parses HTML content
soup = BeautifulSoup(response.text, "html.parser")

headlines = []
# The Chunk of Code below extracts potential headlines (from h1, h2, h3 tags)
for tag in ["h1", "h2", "h3"]:
    for h in soup.find_all(tag):
        text = h.get_text().strip()

        # The lines below only add headlines that are longer than 3 words and not duplicates
        if text and len(text.split()) > 3 and text not in headlines:  # filters out junk
            headlines.append(text)

# The line below stores headlines in a DataFrame (like a spreadsheet)
df = pd.DataFrame({"headline": headlines})

# The lines below save results to a CSV file with timestamp in its name
filename = f"headlines_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
df.to_csv(filename, index=False)

# The line below prints a confirmation message of how many headlines we saved
print(f"✅ Saved {len(headlines)} headlines to {filename}")
