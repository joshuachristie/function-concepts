"""
batch processes xml files, extracting sentences containing "function" as well as context (sentence before and after)
"""
import xml.etree.ElementTree as ET
import glob
import pandas as pd
import re
# grobid in batch mode
# java -Xmx4G -jar grobid-core/build/libs/grobid-core-0.6.0-SNAPSHOT-onejar.jar -gH grobid-home -dIn /path/to/input -dOut /path/to/output -exe processFullText

output_dir = '/home/joshua/Downloads/pdfs-20191202T005556Z-001/pdfs/'
xml_files = glob.glob('{}*.xml'.format(output_dir))
paper_names = [re.search('{}(.*).tei.xml'.format(output_dir), xml).group(1) for xml in xml_files]
count = 0
for filename in xml_files:
    tree = ET.parse(filename)
    root = tree.getroot()
    # get abstract and text
    for text in root.iter('{http://www.tei-c.org/ns/1.0}text'):
        txt = ET.tostring(text, encoding='utf8').decode('utf8')
    for abstract in root.iter('{http://www.tei-c.org/ns/1.0}abstract'):
        ab = ET.tostring(abstract, encoding='utf8').decode('utf8')
    # split text on sentences (note this also splits on undesirable things like Fig.)
    abstract_sentences = ab.split('.')
    txt_sentences = txt.split('.')
    # get function sentences and indices (for sentence before/after)
    function_abstract = tuple([(index, sentence + '.') for index, sentence in enumerate(abstract_sentences)\
                               if 'function' in sentence])
    function_txt = tuple([(index, sentence + '.') for index, sentence in enumerate(txt_sentences)\
                               if 'function' in sentence])
    # extract just the sentences
    function_sentences = [sentence[1] for sentence in function_abstract]\
        + [sentence[1] for sentence in function_txt]
    # get sentences before and after
    sentences_before = [abstract_sentences[index[0] - 1] if index[0] > 0 else 'na'\
                        for index in function_abstract] + [txt_sentences[index[0] - 1]\
                                                           if index[0] > 0 else 'na' for index in function_txt]
    sentences_after = [abstract_sentences[index[0] + 1] if index[0] < len(abstract_sentences) - 1 else 'na'\
                       for index in function_abstract] + [txt_sentences[index[0] + 1]\
                                                          if index[0] < len(txt_sentences) - 1 else 'na'\
                                                          for index in function_txt]
    output = pd.DataFrame({'sentence': function_sentences})
    output['sentence_before'] = sentences_before
    output['sentence_after'] = sentences_after
    output.to_csv('{}{}.csv'.format(output_dir, paper_names[count]))
    count += 1
