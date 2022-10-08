import subprocess
from time import sleep
from clicknium import clicknium as cc, locator, ui

def main():
    # open telegram    
    # process = subprocess.Popen("notepad")

    # search a user 
    cc.find_element(locator.telegram.contact_search).set_text("DK H")
    # use enter button to choose the user
    cc.send_hotkey("{ENTER}")
    # add some text 
    cc.find_element(locator.telegram.content).set_text("Hello DK ")
    # click the send button 
    cc.find_element(locator.telegram.contactsend_btn).click()
    

    # search a chanel 
    cc.find_element(locator.telegram.contact_search).set_text("nnn")
    # use enter button to choose the channel
    cc.send_hotkey("{ENTER}")
    # add some text 
    cc.find_element(locator.telegram.content).set_text("Hello Channel")
    # click the send button 
    cc.find_element(locator.telegram.chanelsend_btn).click()




if __name__ == "__main__":
    main()
