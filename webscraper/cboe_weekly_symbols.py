from selenium import webdriver
import pandas as pd
import schedule
import time 

# Automated Downloading of C.B.O.E. Weekly Options Symbols Every Sunday at 12PM
##creating a func, that handles downloading 
def download_symbols():
    ## specifying the path to download the file using the chrome options
    options = webdriver.ChromeOptions()
    ## creating the variable with the right path
    pref = {'download.default_directory': 'webscraper/data'}
    ## adding new path to preferences 
    options.add_experimental_option("prefs", pref)
    ## creating driver with custom chrome option
    driver = webdriver.Chrome(chrome_options=options)
    # CBOE data URL
    url = 'https://www.cboe.com/us/options/symboldir/weeklys_options/?download=csv'
    ### driver gets desired file
    driver.get(url)

    ### timeout for 2 seconds, so the browser will have enough time to download before it gets closed
    time.sleep(2)

    ### quiting the browser after each download 
    driver.quit()


# Scheduling the downloading at desired time using python schedule 
schedule.every().sunday.at("12:00").do(download_symbols)
# schedule.every(10).seconds.do(download_symbols)

## creating a loop that will run our script on above specified time 
while True: 
    schedule.run_pending() 
    time.sleep(1) 
