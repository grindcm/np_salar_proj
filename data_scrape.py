import pandas as pd
import glassdoor_scraper as gs

path = "C:/Users/Corey/Documents/np_salary_proj/chromedriver.exe"

df = gs.get_jobs("nurse practitioner", 15, False, path, 15)
