import spacy
from spacy import displacy

def print_info(doc, tok_width=20, dep_rel_width=30, head_width=20, dependencies_width=40):
    """
    prints information about token and head dependencies
    args:
        doc: spacy doc
        tok_width: width of col 1
        dep_rel_width: width of col 2
        head_width: width of col 3
        dependencies_width: width of col 4
    returns:
        Nothing (prints output to screen)
    """
    print("{:<{}}{:<{}}{:<{}}{:<{}}\n".format("TOKEN", tok_width, "DEPENDENCY RELATION", dep_rel_width,
                                              "HEAD", head_width, "DEPENDENCIES", dependencies_width))
    for token in doc:
        print("{:<{}}{:<{}}{:<{}}{}".format(
            token.text, tok_width, str(spacy.explain(token.dep_)), dep_rel_width,
            token.head.text, head_width, [child for child in token.children]))

def show_dependency_graph(doc, width):
    displacy.render(doc, style="dep", jupyter=True, options={'distance' : width})

def visualise(doc, width=100):
    #print_info(doc)
    show_dependency_graph(doc, width)
