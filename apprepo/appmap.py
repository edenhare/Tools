import json
import os
import sys
#
# you must have graphviz installed for pygraphviz to work
import pygraphviz as pgv


__DEBUG__ = True


def getJSON(**kwargs):
    """
    getJSON - take the provided json file and return the parsed and sorted keys
    parameters: get=filename.json
    return: JSON sting
    """

    global __DEBUG__
    if __DEBUG__ == True:
        print(f"getJSON: kwargs={kwargs}")
    
    get = kwargs['get']
    
    with open(get, 'r') as handle:
        parsed = json.load(handle)
        if __DEBUG__ == True:
            print(json.dumps(parsed, indent=4, sort_keys=True))
    
    return(parsed)
  
def getDetails(**kwargs):
    """
    getDetails - get the app details from the jSON string
    paramters: get=json string
    return: all keys and values for the Details key
    
    NOTE: as new keys and values are added to the details key, they need
    to be added here to be displayed
    """
    
    app = kwargs['get']
     
    for k,v in app.items():
        
        if k == 'Details':
            rDetails = (f"<h1>{k}</h1>\n"
            f"<h2>Application Name: {appData['Details']['Name']}</h2>\n"
            f"<h2>Application ID: {appData['Details']['Identifier']}</h2>\n"
            f"<h2>Description: {appData['Details']['Description']}</h2>\n"
            f"<h2>Department: {appData['Details']['Department']}</h2>\n"
            )
            
    return(rDetails)
        
def getContacts(**kwargs):
    """
    getContacts - get the list of contacts for the app
    paramters: get=json string
    return: all keys and values for the Contacts key
    
    NOTE: as new keys and values are added to the contacts key, they need
    to be added here to be displayed
    """
    
    app = kwargs['get']
     
    for k,v in app.items():
        if k == "Contacts":
            rContacts = (f"<h1>{k}</h1>\n"
            f"<h2>Business Owner: {appData['Contacts']['BusOwner']}</h2>\n"
            f"<h2>Application ID: {appData['Contacts']['ITOwner']}</h2>\n"
            )
    
    return(rContacts)        

def getData(**kwargs):
    """
    getData - get the list of data for the app
    paramters: get=json string
    return: all keys and values for the Data key
    
    NOTE: as new keys and values are added to the data key, they need
    to be added here to be displayed
    """
    app = kwargs['get']
     
    for k,v in app.items():
        if k == "Data":
            rData = (f"<h1>{k}</h1>\n"
            f"<h2>Data Classification: {appData['Data']['Classification']}</h2>\n"
            f"<h2>Data Type: {appData['Data']['DataType']}</h2>\n"
            f"<h2>Data Owner: {appData['Data']['DataOwner']}</h2>\n"
            )
            
    return(rData)
    
    
def getNeighbors(**kwargs):
    """
    getNeighbors - get the list of neighbors for the app
    paramters: 
            get=json string
            map=True|False
    return: all keys and values for the Neighbors key
    
    NOTE: as new keys and values are added to the Neighbors key, they need
    to be added here to be displayed
    """
    app = kwargs['get']
    map = kwargs['map']
     
    for k,v in app.items():
        rNeighbors = ""
        if k == "Neighbors":
            rNeighbors = (f"<h1>{k}</h1>\n")
            for x,y in appData['Neighbors'].items():
                tmp = (f"<h2>Name: {appData['Neighbors'][x]['Name']}\n"
                f"<h2>Identifer: {appData['Neighbors'][x]['Id']}\n"
                f"<h2>Data Flow: {appData['Neighbors'][x]['Flow']}\n"
                f"<h2>Request Method: {appData['Neighbors'][x]['RequestMethod']}\n"
                f"<h2>Request Size: {appData['Neighbors'][x]['RequestSize']}\n"
                f"<h2>Requests Per Hour: {appData['Neighbors'][x]['RequestsPerHour']}\n"
                f"<h2>Authentication: {appData['Neighbors'][x]['Authentication']}\n"
                )
                
                rNeighbors = rNeighbors + tmp
    
    return rNeighbors
    

def buildAppMapFile(**kwargs):
    """
    buildAppMapFile - create the app map only for the named application
    paramters: 
    output: 
        appname.dot - the DOT language file
        appname.png - a PNG of the map
    return: Nonw
    """
    pass
    G=pgv.AGraph(strict=False,directed=True)

    G.add_node('a') # adds node 'a'
    G.add_edge('b','c') # adds edge 'b'-'c' (and also nodes 'b', 'c')
    G.node_attr['shape']='circle'
    G.edge_attr['color']='red'
    G.graph_attr['label']='Name of graph'
    s=G.string()
    G.write("file.dot")
    G.draw('file.png')  # write previously positioned graph to PNG file
    G.draw('file.ps',prog='circo') # use circo to position, write PS file


def loadAppJSON(**kwargs):

    """
    getContacts - get the list of contacts for the app
    paramters: get=json string
    return: all keys and values for the Contacts key
    
    NOTE: as new keys and values are added to the details key, they need
    to be added here to be displayed
    """
    global __DEBUG__
    
    app = kwargs['get']
 
    if __DEBUG__ == True:
        print(f"loadAppJSON: kwargs={kwargs}")
    #
    # get the JSON data
    #
    appData = getJSON(get=app)
        
    return appData    
    
    
def getSummary(**kwargs):
    """
    getContacts - get the list of contacts for the app
    paramters: get=json string
    return: all keys and values for the Contacts key
    
    NOTE: as new keys and values are added to the details key, they need
    to be added here to be displayed
    """
    appData = kwargs['get']
     
    
    result = ""
    
    rDetails = getDetails(get=appData)
    rContacts = getContacts(get=appData)
    rData = getData(get=appData)
    rNeighbors = getNeighbors(get=appData)
    
    print(rDetails)
    print(rContacts)
    print(rData)
    print(rNeighbors)
    
    buildAppMapFile()

    return


def unit_test():
    """
    getContacts - get the list of contacts for the app
    paramters: get=json string
    return: all keys and values for the Contacts key
    
    NOTE: as new keys and values are added to the details key, they need
    to be added here to be displayed
    """
    print("running unit tests")
    return

if __name__ == "__main__":
    """
    getContacts - get the list of contacts for the app
    paramters: get=json string
    return: all keys and values for the Contacts key
    
    NOTE: as new keys and values are added to the details key, they need
    to be added here to be displayed
    """
    #
    # Validate if we have any arguments
    #
    print(len(sys.argv))
    if len(sys.argv) == 1:
        unit_test()
        sys.exit(0)
    elif len(sys.argv) < 1:
        #
        # No template on comand line, quit
        #
        print(f"Usage: {sys.argv[0]} file(s)")
        sys.exit(1)
    
    for x in range(1,len(sys.argv)):
        print(f"printing {sys.argv[x]}")
        #
        # get the JSON data
        #
        appData = loadAppJSON(get=sys.argv[x]+".json")
    
        result = getSummary(get=appData)    

    sys.exit(0)    
