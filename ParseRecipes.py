#!/usr/bin/python
# ParseRecipe.csv to html
# Author(s): Dad and Tara
# Version 1 - added css class to all columns except header
  
import sys
import csv
import operator
  
if len(sys.argv) < 3:
    print ("Usage: csvToTable.py csv_file html_file")
    exit(1)
 
# csv format: title, instructions, tag, order 
 
# Open the CSV file for reading
reader = csv.reader(open(sys.argv[1]))

# sort csv file
sortedreader = sorted(reader, key=operator.itemgetter(2,0))

# Create the HTML file for output
htmlfile = open(sys.argv[2],"w")
 
# initialize rownum variable
rownum = 0
prevTag = ''

# Style Header
htmlfile.write('''<ul><style type="text/css"> 
                        h1 {f   ont-weight:bold;font-size:20  px}
                        h2 {f   ont-weight:bold;font-size:16  px}
                        li {font-weight:normal;font-size:14px;list-style-type: none;} 
                        li.recipe-heading {font-weight:bold;font-size:14px;padding-left:5px;padding-top:10px;list-style-type: none;} 
                        li.recipe-instructions {font-weight:normal;font-size:12px;padding-left:10px;list-style-type: none;}
                        li.recipe-tag {font-weight:normal;font-style:italic;font-size:11px;padding-left:5px;padding-top:3px;}
                        li.recipe-tag-heading{font-weight:bold;font-size:16px;padding-left:0px;padding-top:20px;padding-bottom:5px;list-style-type: none;}
                    </style>''')
                    
                    
# write <table> tag
htmlfile.write('<h1>Porter Recipes</h1>')
htmlfile.write('<h2>Table of Contents</h2>')
htmlfile.write('<ul>')

# generate table contents
for row in sortedreader: # Read a single row from the CSV file
    # if first row or tag has changed, write tag as heading
    if rownum == 0:
        htmlfile.write('<li class="recipe-tag-heading">' + row[2] + '</li>')
    elif row[2] != prevTag:
        htmlfile.write('<li class="recipe-tag-heading">' + row[2] + '</li>')
    
    htmlfile.write('<li class="recipe-heading"><a href="#row' + str(rownum) + '">' + row[0].replace('\n', '<br />') + '</a></li>')
    # write header row. assumes first row in csv contains header
    # for column in row:
        # htmlfile.write('<li>' + column + '</li>')
     
    prevTag = row[2]
    #increment row count    
    rownum += 1
    
htmlfile.write('</ul>')
rownum = 0

# write <table> tag
htmlfile.write('<ul>')

# generate table contents
for row in sortedreader: # Read a single row from the CSV file
    # if first row or tag has changed, write tag as heading
    if rownum == 0:
        htmlfile.write('<li class="recipe-tag-heading">' + row[2] + '</li>')
    elif row[2] != prevTag:
        htmlfile.write('<li class="recipe-tag-heading">' + row[2] + '</li>')
    
    htmlfile.write('<a name="row' + str(rownum) + '" /><li class="recipe-heading">' + row[0].replace('\n', '<br />') + '</li>')
    htmlfile.write('<li class="recipe-instructions">' + row[1].replace('\n', '<br />') + '</li>')
    # write header row. assumes first row in csv contains header
    # for column in row:
        # htmlfile.write('<li>' + column + '</li>')
     
    prevTag = row[2]
    #increment row count    
    rownum += 1

htmlfile.write('</ul>')
 
# print results to shell
print ("Created " + str(rownum) + " row table.")
exit(0)