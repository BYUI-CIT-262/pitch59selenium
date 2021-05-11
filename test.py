from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import sys, getopt


def main(argv):
   global driver 
   try:
      opts, args = getopt.getopt(argv,"h")
   except getopt.GetoptError:
      print ('err')
      sys.exit(2)
      
   for opt, arg in opts:
      if opt in ['-h']:
         driver = webdriver.Remote("http://127.0.0.1:4444/wd/hub", DesiredCapabilities.CHROME, options=options)
         print('driver')
      else:
         driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)
         print('driver')
         return driver
        
if __name__ == "__main__":
   print(main(sys.argv[1:]))





# /------------------------------------------------------------------/
# def main(argv):
#    inputfile = ''
#    outputfile = ''
#    try:
#       opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
#    except getopt.GetoptError:
#       print ('test.py -i <inputfile> -o <outputfile>')
#       sys.exit(2)
#    for opt, arg in opts:
#       if opt == '-h':
#          print ('test.py -i <inputfile> -o <outputfile>')
#          sys.exit()
#       elif opt in ("-i", "--ifile"):
#          inputfile = arg
#       elif opt in ("-o", "--ofile"):
#          outputfile = arg
#    print ('Input file is "', inputfile)
#    print ('Output file is "', outputfile)

# if __name__ == "__main__":
#    main(sys.argv[1:])