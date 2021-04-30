import sys, getopt


def main(argv):
   option = False
   try:
      opts, args = getopt.getopt(argv,'h','headless=')
   except getopt.GetoptError:
      print ('err')
      sys.exit(2)
      
   for opt, arg in opts:
      if opt in ['-h','--headless']:
         option = True
         print('option = true')
         sys.exit()
      elif opt != '-h':
         print('nononoo')
        
if __name__ == "__main__":
   main(sys.argv[1:])





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