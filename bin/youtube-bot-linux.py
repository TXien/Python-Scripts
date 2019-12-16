import time
import webbrowser
import os

url = "https://www.youtube.com/watch?v=D2aRUCRtJME"#str(input("Enter your video url in ->\"url here \"<-  : "))
n = "3"#input("Enter refresh rate(seconds) : ")
brow = "chrome"#input("Enter your default browser in ->\"browser here \"<-  : ")
while (1):
    os.system(" killall -9 " + brow)
    time.sleep(int(n))
    webbrowser.open(url)
    print('Successfully Viewd')
