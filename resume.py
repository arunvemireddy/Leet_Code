
from selenium import webdriver

# Configure Selenium to use a webdriver of your choice (e.g., ChromeDriver)
driver = webdriver.Chrome()

# Set a custom user-agent to override the default user-agent used by Selenium
custom_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={custom_user_agent}")

# Launch the browser with the customized options
driver = webdriver.Chrome(options=options)

# Now you can navigate to the website and perform scraping operations
driver.get("https://www.overleaf.com/project/63f52dccb0ee2d3312e6ca32")

# Perform scraping actions using Selenium's methods
# ...

# Close the browser session when you're done
driver.quit()