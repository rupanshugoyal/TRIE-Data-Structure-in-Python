# maths project
# implementation of trie data structure wrt. the problem statement
# author : rupanshu goyal and others

class fraction: #OK
    def __init__(self, numerator, denominator):
        self.numerator      = numerator
        self.denominator    = denominator
        
    def __str__(self):
        return str( " (" + str(self.numerator) +"/" + str(self.denominator) + ") " )

    def addToNumerator(self):
        self.numerator += 1
        
    def addToDenominator(self):
        self.denominator += 1 
        
class listitem: #OK
    def __init__(self, trienode, probability):
        self.trienode       = trienode
        self.probability    = probability
        
    def __repr__(self):
        return str( " ("+ str(self.trienode) + "," + str(self.probability) +") " )
        
class trienode: #OK
    def __init__(self, boxnum):
        self.boxnum     = boxnum
        self.nextnodes   = list()
    
    def __repr__(self):
        return str(" (" + str(self.boxnum) +" next to "+ str(self.nextnodes) +") ")
    
    def addPath(self , thispath):
        current = self # maintain a current node pointer
        flag = False #that the current node is present in current.nextlist
        
        for element in thispath: 
            changed = False
            
            if(not flag):
                
                if( len(current.nextnodes) != 0):
                    
                    for litem in current.nextnodes:
                        litem.probability.addToDenominator()
                        
                        if( element == litem.trienode.boxnum ):
                            litem.probability.addToNumerator()
                            current = litem.trienode
                            changed = True
                
                else:
                    flag = True
            
            if(flag or not changed):
                denom = 1
                
                if( len(current.nextnodes) != 0 ):
                    denom = current.nextnodes[0].probability.denominator
                
                newnode = trienode(element)
                current.nextnodes.append( listitem( newnode , fraction(1, denom )) )
                current = newnode

    
root = trienode(0)
try:
    datafile    = open("datasetsize50.txt", "r")
    filedata    = datafile.read()
    paths       = list(filedata.split("\n"))
    for path in paths:
        pathstr     = path[1:len(path)-1]
        pathlist    = list(map(int, pathstr.split(",")))
        print(pathlist)
        root.addPath(pathlist)
        print(root)
except Exception as e:
    print(e)