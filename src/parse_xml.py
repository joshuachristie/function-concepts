import xml.etree.ElementTree as ET

# can probably just look through abstract and body tags (latter might be element 'text')
# wouters2003.pdf.tei.xml

tree = ET.parse('/home/joshua/Downloads/wouters2003.pdf.tei.xml')
root = tree.getroot()

for text in root.iter('{http://www.tei-c.org/ns/1.0}text'):
    txt = ET.tostring(text, encoding='utf8').decode('utf8')

for abstract in root.iter('{http://www.tei-c.org/ns/1.0}abstract'):
    ab = ET.tostring(abstract, encoding='utf8').decode('utf8')
    
function_abstract = [sentence + '.' for sentence in ab.split('.') if 'function' in sentence]
function_txt = [sentence + '.' for sentence in txt.split('.') if 'function' in sentence]

# for appending to excel sheet: https://stackoverflow.com/questions/38074678/append-existing-excel-sheet-with-new-dataframe-using-python-pandas
