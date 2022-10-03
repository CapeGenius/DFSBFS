# Rohan Bendapudi - 10/2/22 (hopefully submitted before midnight at Boston)
'''
DFS: really fun recursion
BFS: really shouldn't have done recursion


BFS Original Algorithm:

    - create a universal queue with all nodes added to it ordered by layer sequentially
    - use a recursive method to stack each layer
        - iterate through each child node and add it to the list
        - in that iteration, call this method again to add children from current layer to the queue

    post condition: this implementation will automatically organize into a layer-based organized queue

I want to include my BFS pseudocode from my notebook because I thought it was rather complex 
and deviated heavily implementation-wise from my original plan. I think it transformed more into
a queue solution implemented through recursion which made the recursion somewhat unecessary, but I'm really glad
I explored this method. The problem with my original algorithm was that each iteration was organizing the nodes
by their respective children nodes rather than the entire layer, fragmenting the intended layer-based BFS organization 
        
'''


# create the tree node class
class TreeNode:

    # declares the attributes
    data = None
    childrenNodes = []

    # declares the node
    def __init__(self, data):
        self.data = data
        self.childrenNodes = []       

# first layer of tree
root = TreeNode("C:")
documents = TreeNode("documents")
application = TreeNode("application")
desktop = TreeNode("desktop")
root.childrenNodes.append(documents)
root.childrenNodes.append(application)
root.childrenNodes.append(desktop)

#second layer of tree
marcel = TreeNode("marcel.jpg")
jay = TreeNode("jay.pdf")
saurya = TreeNode("saurya")
compSciIA = TreeNode("csIA")
ariya = TreeNode("ariya")
temi = TreeNode("temi")
ansari = TreeNode("mr.ansari")
kishan = TreeNode("bishan.app")

application.childrenNodes.append(marcel)
application.childrenNodes.append(jay)
application.childrenNodes.append(saurya)
desktop.childrenNodes.append(compSciIA)
desktop.childrenNodes.append(TreeNode("shikhar"))
desktop.childrenNodes.append(TreeNode("abhinav.jpg"))
desktop.childrenNodes.append(ariya)
documents.childrenNodes.append(temi)
documents.childrenNodes.append(ansari)
documents.childrenNodes.append(kishan)

#third layer of tree
isaac = TreeNode("isaac")
landen = TreeNode("landen.pdf")
michael = TreeNode("michael.png")
lascaudian = TreeNode("lascaudian.jpg")
akshat = TreeNode("akshat.pdf")
xiao = TreeNode("xiao")
ahmed = TreeNode("ahmed.pdf")
saurya.childrenNodes.append(isaac)
saurya.childrenNodes.append(landen)
temi.childrenNodes.append(michael)
temi.childrenNodes.append(lascaudian)
compSciIA.childrenNodes.append(akshat)
compSciIA.childrenNodes.append(xiao)
compSciIA.childrenNodes.append(ahmed)

# declares lists of paths with pdf
pathNamesList = []

# depth first search for algorithm
def DepthFirstSearch(c, pathName):


    # iterate through each child node per node
    for x in range(len(c.childrenNodes)):
        print(len(c.childrenNodes))

        # the file with the pdf extension will be saved to a data structure
        if (".pdf" in c.childrenNodes[x].data):
            pathNamesList.append(pathName + "/" + c.data + "/" + c.childrenNodes[x].data)

        # checks file name
        nodeName = str(c.childrenNodes[x].data)
        print("x is " + str(x))

        # the node is not a file
        if ((".pdf" and ".jpg" and ".png" and ".app") not in nodeName and x == 0):
            DepthFirstSearch(c.childrenNodes[x], pathName + "/" + c.data)

        # the node is not a file
        if ((".pdf" and ".jpg" and ".png" and ".app") not in nodeName and x > 0):
            DepthFirstSearch(c.childrenNodes[x], pathName + "/" + c.data)

# global access variable to add all matching paths with pdf extension in BFS 
searchList = []


# searches through layer to find pdf extension
def BFSSearch(layerQueue):

    # iterates through all the nodes in current layer, searching for PDF extension
    for x in range(len(layerQueue)):
        print(layerQueue[x].data)

        # adds node data to list of node paths that have pdf extension
        if (".pdf" in layerQueue[x].data):
            searchList.append(layerQueue[x].data)

# creates (or explodes) a new list of nodes on a layer queue from the queue of parents 
def ListExplosion(parentNodesList):
    
    # declares a new layer of nodes
    childLayerQueue = []

    # for loop to iterate through each parent node from previous layer queue and  create a child list
    for x in range(len(parentNodesList)):

        # iterates through each child and adds it to a new layer 
        for y in range(len(parentNodesList[x].childrenNodes)):
            memberNode = parentNodesList[x].childrenNodes[y]

            # pass the parent directory to the child node data
            memberPath = parentNodesList[x].data + "/" + parentNodesList[x].childrenNodes[y].data
            memberNode.data = memberPath

            # adds the child node to the layer
            childLayerQueue.append(memberNode)

    # ends the recursion if there is no more nodes to be checked (base case)
    if (len(childLayerQueue) == 0):
        return 0

    # otherwise checks to see if current layer holds a pdf extension and moves on to create the next layer 
    else:
        BFSSearch(childLayerQueue)
        ListExplosion(childLayerQueue)
    '''BFSSearch(newQueue)
    print(tempList)'''

#initializes the BFS process by preparing the root children into a list
def InitializeBFS(c):
    
    # initializes a list for the top layer
    topLayer = []

    # for loop to iterate through all the children and add it to the layer
    for x in range(len(root.childrenNodes)):

        # passes previous path of parent nodes to children nodes 
        c.childrenNodes[x].data = c.data + "/" + c.childrenNodes[x].data 

        # adds all the child nodes to the top layer
        topLayer.append(root.childrenNodes[x])
    
    #print(topLayer)

    # calls ListExplosion method to recursively create a new list of the next layer using the top layer
    ListExplosion(topLayer)

#main method to run DFS and BFS
def main():
    #begins DFS process
    DepthFirstSearch(root, "")

    #begins BFS process
    InitializeBFS(root)

main()

# path names for DFS
print(pathNamesList)

# path names for BFS
print(searchList)
