We're finally starting to build some mini-projects! For the 2 tasks below, ensure they're in different folders.

# 1.0 Working with APIs
In summary, we produced a simple script that called the [Frankfurter API](https://frankfurter.dev/) to get all the exchange rates.

We first set up a [virtual environment](https://www.youtube.com/watch?v=N5vscPTWKOk) `.venv` which we did in the terminal below:
```bash
python -m venv .venv # Make virtual environment
.\venv\Scripts\activate.bat # Activate the virtual environment

pip install requests # Install the requests library
```
**NOTE:** Do ensure you're running everything from the CMD (not Powershell). You can look this up at the top right of your terminal (next to the '+' button).
 
We then produced the following Python script, `exchange_rates.py`:

```python
import requests

iso_codes = requests.get("https://api.frankfurter.app/currencies")
iso_codes_only = list(iso_codes.json().keys())
print(iso_codes_only)
print("")

amount=600
from_currency = "MYR"
to_currency = "GBP"
response = requests.get(f'https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}')
print(f"Status code: {response.status_code}")
print(response.json())
```

**This week, please do the following:**
- Read what HTTP endpoints and how data transferred across APIs: https://www.datacamp.com/tutorial/making-http-requests-in-python
- Augment the above script with the following:
    - Functionality for a user to input the currency code they want to convert from & to via Terminal. **Hint:** Use Python's `.input()` function.
    - Try-except blocks if the inputted currency code isn't in the `iso_codes_only` list (or not available in the [list of currencies in the API](https://api.frankfurter.app/currencies)).
- Yes, yes. Please use ChatGPT to augment your learning but make sure you understand every component. Add 'explain step-by-step' into your prompts!

# 2.0 Doing Data Analysis
We're going to briefly introduce the tools Data Scientists use on the job. We were recently introduced to Jupyter Notebooks, which are tools Data Scientists use to analyze data. For simplicity, please use [Google Colab](https://colab.research.google.com/) (not VSCode). A brief tutorial for the tool can be found [here](https://www.youtube.com/watch?v=8KeJZBZGtYo).

Our goal will be to use the below datasets (which **you need to download and upload to Google Colab**) to follow along with tutorials:
- Tutorial 1 - A Gentle Introduction to Pandas Data Analysis: https://www.youtube.com/watch?v=_Eb0utIRdkw
- Dataset 1 - Use this dataset for Tutorial 1: [MrBeast_youtube_stats](/week3/datasets/MrBeast_youtube_stats.csv)
- Tutorial 2 - Exploratory Data Analysis with Pandas Python: https://www.youtube.com/watch?v=xi0vhXFPegw&t=198s
- Dataset 2 - Use this dataset for Tutorial 2: [coaster_db](/week3/datasets/coaster_db.csv)
