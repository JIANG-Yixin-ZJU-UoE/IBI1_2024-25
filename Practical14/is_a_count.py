# Goal: to count the number of "is_a" in go_obo.xml using DOM and SAX and compare the time spent by each method
# Procedure:
# 1. import necessary modules
# 2. use DOM parser, start the timer and parse the XML file
# 3. use SAX parser to parse the XML file
# 4. compare the time spent by each method

import xml.dom.minidom            # import DOM module
import xml.sax                    # import SAX module
from datetime import datetime     # use datetime module to count time

# DOM parser
def parse_with_dom(xml_file):
    start_time = datetime.now()   # start the timer
    # store the result using a dictionary
    results = {
        "molecular_function": {"term_id": "", "term_name": "","count": 0},
        "biological_process": {"term_id": "", "term_name": "", "count": 0},
        "cellular_component": {"term_id": "", "term_name": "", "count": 0}}
    
    dom_tree = xml.dom.minidom.parse(xml_file)       # parse the XML file
    terms = dom_tree.getElementsByTagName("term")    # get all the term nodes
    
    # get namespaces
    for term in terms:
        namespace = term.getElementsByTagName("namespace")[0].firstChild.nodeValue
        
        # count the number of is_a
        is_a_count = len(term.getElementsByTagName("is_a"))
        
        # update the results in the dictionary to make sure the dictionary contains the largest number of is_a
        if is_a_count > results[namespace]["count"]:
            results[namespace]["count"] = is_a_count        # update the count
            term_name = term.getElementsByTagName('name')[0].firstChild.nodeValue
            term_id = term.getElementsByTagName('id')[0].firstChild.nodeValue
            results[namespace]["term_id"] = term_id         # update the term_id
            results[namespace]["term_name"] = term_name     # update the term_name
            
    end_time = datetime.now()                                # end the timer
    return results, (end_time - start_time).total_seconds()  # count the time used 

# SAX parser
class GOHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current_tag = None
        self.content_buffer = ""  # last time I used too many variables, which overwhelmed the computer. this time use the buffer to prevent this
        self.current_term = None
        self.results = {
            "molecular_function": {"term_id": "", "term_name": "", "count": 0},
            "biological_process": {"term_id": "", "term_name": "", "count": 0},
            "cellular_component": {"term_id": "", "term_name": "", "count": 0}}
    
    def startElement(self, tag, attrs):
        self.current_tag = tag
        if tag == "term":
            # initialize the current term
            self.current_term = {
                "name": "",
                "id": "",
                "namespace": "",
                "is_a_count": 0 }
        # count the number of is_a
        elif tag == "is_a" and self.current_term:
            self.current_term["is_a_count"] += 1 
    
    def endElement(self, tag):
        if tag == "term":
            # get the namespace
            if self.current_term and self.current_term["namespace"] in self.results:
                namespace = self.current_term["namespace"]
                # update information in the results dictionary
                if self.current_term["is_a_count"] > self.results[namespace]["count"]:
                    self.results[namespace]["term_id"] = self.current_term["id"]
                    self.results[namespace]["term_name"] = self.current_term["name"]
                    self.results[namespace]["count"] = self.current_term["is_a_count"]
            # re-initialize the current term
            self.current_term = None
        elif self.current_term:
            # store the contents in the content_buffer into the current_term
            if tag == "id":
                self.current_term["id"] = self.content_buffer.strip()
            elif tag == "name":
                self.current_term["name"] = self.content_buffer.strip()
            elif tag == "namespace":
                self.current_term["namespace"] = self.content_buffer.strip()
        
        # empty the content_buffer
        self.content_buffer = ""
    
    def characters(self, content):
        # get the text content
        if self.current_tag in ["id", "name", "namespace"]:
            self.content_buffer += content

def parse_with_sax(xml_file):
    start_time = datetime.now()  # start the timer
    handler = GOHandler()
    xml.sax.parse(xml_file, handler)
    end_time = datetime.now()    # end the timer
    return handler.results, (end_time - start_time).total_seconds() # count the time used

# compare DOM and SAX
if __name__ == "__main__": 
    xml_is_a = "go_obo.xml"
    
    # parse the XML file using DOM and SAX
    dom_results, dom_time = parse_with_dom(xml_is_a) 
    sax_results, sax_time = parse_with_sax(xml_is_a)
    
    print("terms with the most <is_a> in each ontology:")
    
    print("DOM results:")
    for ontology, data in dom_results.items():
        print(f"{ontology.replace('_', ' ').title()}:")
        print(f"term_id: {data['term_id']}")
        print(f"term_name: {data['term_name']}")
        print(f"number of <is_a>: {data['count']}\n")

    print("SAX results:")
    for ontology, data in sax_results.items():
        print(f"{ontology.replace('_', ' ').title()}:")
        print(f"term_id: {data['term_id']}")
        print(f"term_name: {data['term_name']}")
        print(f"number of <is_a>: {data['count']}\n")
    
    print(f"DOM spent: {dom_time:.4f} seconds")
    print(f"SAX spent: {sax_time:.4f} seconds")
    if dom_time > sax_time:
        print("SAX is faster than DOM")
    elif dom_time < sax_time:
        print("DOM is faster than SAX")
    else:
        print("DOM and SAX are equally fast")
# SAX is faster than DOM
