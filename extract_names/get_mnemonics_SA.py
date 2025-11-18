from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Set path to chromedriver as per your configuration
chromedriver_path = '/usr/lib/chromium-browser/chromedriver'  # Change this to the path where you have your chromedriver

# Initialize the Chrome driver service
webdriver_service = Service(chromedriver_path)

# Choose Chrome Browser
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

# Open the website
driver.get("https://mast.stsci.edu/portal/Mashup/Clients/JwstEdb/JwstEdb.html")

try:
    # Function to search and save suggestions for a given term
    def search_and_save(term, suggestions_list):
        # Wait until the input element is present
        wait = WebDriverWait(driver, 20)
        input_box = wait.until(EC.presence_of_element_located((By.ID, "combo-1085-inputEl")))

        # Clear the input field
        input_box.clear()

        # Enter the search term into the input field
        input_box.send_keys(term)

        # Wait for the suggestions to load
        time.sleep(5)  # You might need to adjust this sleep time based on your internet speed and response time of the website

        # Locate the suggestions
        suggestions = driver.find_elements(By.CSS_SELECTOR, ".x-boundlist-item")

        # Filter suggestions to include only those starting with the search term and convert to uppercase
        filtered_suggestions = [suggestion.text.upper() for suggestion in suggestions if suggestion.text.startswith(term.upper())]

        # Append the filtered suggestions to the main list
        suggestions_list.extend(filtered_suggestions)

        # Append filtered suggestions to a text file
        with open('suggestions_SA.txt', 'a') as file:
            file.write(f"Suggestions for '{term}':\n")
            for suggestion in filtered_suggestions:
                file.write(suggestion + '\n')
            file.write('\n')

    # List to hold all suggestions
    all_suggestions = []

    # Perform searches for the specified terms
    search_and_save("SA", all_suggestions)
    
    # Save all suggestions to a CSV file
    with open('suggestions_SA.csv', 'w') as csv_file:
        csv_file.write(','.join(all_suggestions))

finally:
    # Close the browser
    driver.quit()

