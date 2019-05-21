#!/usr/bin/env python3

def makehtml(resultInput, htmlInput):
  fResult= open(resultInput,"r")  #read result file 
  fHtml = open(htmlInput, "r")  #read desired html file to output
  #if f.mode == "r":
  contentResult = fResult.read()
  contentHtml = fHtml.read()
  #print(contentResult)  #this line for testing only
  
  f = open('dencrime.html', 'w')
  f.write(contentHtml)
 
  message = """<footer>"""+ contentResult + """</footer>
  </html>"""

  f.write(message)
  f.close()
  fResult.close()
  fHtml.close()
  return 0

#makehtml("userResult.txt","htmlInputfile.html")

