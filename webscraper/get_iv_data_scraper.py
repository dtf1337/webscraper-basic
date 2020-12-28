import csv
from selenium import webdriver
import pandas as pd
import login
import time

  ### creating driver
driver = webdriver.Chrome()


# Login automation func
def loginfunc():
     ## Login page URL
    login_url = 'https://www.ivolatility.com/login.j'
    ## opening the login page
    driver.get(login_url)
    ## getting the username and sending the keys
    driver.find_element_by_xpath('/html/body/div/div/div[3]/div[2]/div/form/div[1]/div[2]/input[1]').send_keys(login.LOGIN_IV_DATA)
    ## getting the password and sending the keys
    driver.find_element_by_xpath('/html/body/div/div/div[3]/div[2]/div/form/div[1]/div[3]/input').send_keys(login.PASS_IV_DATA)
    ## getting the login button and clicking it
    driver.find_element_by_xpath('/html/body/div/div/div[3]/div[2]/div/form/div[1]/div[5]/button').click()
    ## make the browser wait for one second, so it will have enough time to login properly
    time.sleep(1)
  

# IV index data automation func
def getIVData(input):
    ## IV index url 
    url = 'https://www.ivolatility.com/options.j?ticker='+input+'&R=1'
    ## going to iv data page after login
    driver.get(url)
    ## make the browser wait for one second, so the data will get loaded 
    time.sleep(1)
    # Getting xPaths Of Tables Using xPath And Attaching The ".text" Method, So We Get Value Of Each Table
    ## IV Index call data
    ### current value
    iv_ind_call_cur_val = driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div[2]/table[1]/tbody/tr[3]/td/table[2]/tbody/tr[7]/td[2]/font').text
    ### 52 wk High/Date 
    iv_ind_call_ftwh_val = driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div[2]/table[1]/tbody/tr[3]/td/table[2]/tbody/tr[7]/td[5]/font').text
    ### 52 wk Low/Date
    iv_ind_call_ftwl_val = driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div[2]/table[1]/tbody/tr[3]/td/table[2]/tbody/tr[7]/td[6]/font').text
    
    ## IV Index put data
    ### current value
    iv_ind_put_cur_val = driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div[2]/table[1]/tbody/tr[3]/td/table[2]/tbody/tr[8]/td[2]/font').text
    ### 52 wk High/Date 
    iv_ind_put_ftwh_val = driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div[2]/table[1]/tbody/tr[3]/td/table[2]/tbody/tr[8]/td[5]/font').text
    ### 52 wk Low/Date
    iv_ind_put_ftwl_val = driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div[2]/table[1]/tbody/tr[3]/td/table[2]/tbody/tr[8]/td[6]/font').text
    
    ## IV Index mean data
    ### current value
    iv_ind_mean_cur_val = driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div[2]/table[1]/tbody/tr[3]/td/table[2]/tbody/tr[9]/td[2]/font').text
    ### 52 wk High/Date     
    iv_ind_mean_ftwh_val = driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div[2]/table[1]/tbody/tr[3]/td/table[2]/tbody/tr[9]/td[5]/font').text
    ### 52 wk Low/Date   
    iv_ind_mean_ftwl_val = driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div[2]/table[1]/tbody/tr[3]/td/table[2]/tbody/tr[9]/td[6]/font').text

    ### getting the symbol data xpath to output it along with an iv data
    symbol_info = driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div[2]/table[1]/tbody/tr[1]/td/form/table/tbody/tr[3]/td/b/span').text
  
    # Calculatin the year from month,day info
    



    ### outputting the row with iv index call data + symbol  
    call_raw = iv_ind_call_cur_val + ' ' + iv_ind_call_ftwh_val + ' ' + iv_ind_call_ftwl_val + ' - ' + symbol_info
    ### outputting the row with iv index put data + symbol  
    put_raw = iv_ind_put_cur_val + ' ' + iv_ind_put_ftwh_val + ' ' + iv_ind_put_ftwl_val + ' - ' + symbol_info
    ### outputting the row with iv index call data + symbol  
    mean_raw = iv_ind_mean_cur_val + ' ' + iv_ind_mean_ftwh_val + ' ' + iv_ind_mean_ftwl_val + ' - ' + symbol_info

    print(call_raw)
    print(put_raw )
    print(mean_raw)
# Getting the csv file
with open('/home/user/Desktop/projects/trading-platform/webscraper/data/cboesymboldirweeklys.csv', 'r') as csv_file:
    ## reading the data from a csv file
    symbols = csv.reader(csv_file)
    ## our csv contains the header, so we need to start our loop from the second line
    header = next(symbols)
    #Running the login function only once, so we will run this script on the same browser session and won't exide the limit of login attempts
    loginfunc()
    # if statement to check if the csv has the header, so the script will automatically skip the header a start running from the second line
    if header != None:
        ## runing through each symbol within our csv file
        for symbol in symbols:
            ## replacing dots to forward slash in each symbol, so we won't get error
            upd_symbol = symbol[1].replace('.', '/')
            ## getting the second item in a row, which is the symbol
            getIVData(upd_symbol)
            ## make the browser wait after eact iteration through the list of symbols for two seconds, so the data from each symbol will get loaded fully
            time.sleep(2)
driver.quit()