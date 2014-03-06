class Properties(object):
    lines = ""
    properties = {}

    #Constructor for class. Requires that the filepath is entered
    def __init__(self, filepath):
        if(filepath != ""):
            prop_file = open(filepath, "r")
            self.lines = prop_file.read().split('\n')
            for ln in self.lines:
                
                eqind = ln.index('=')
                prop = ln[:eqind]
                prop = prop.strip()
                val = ln[eqind+1:]
                val = val.strip()
                self.properties[prop] = val

    def getProperty(self, prop):
        return self.properties[prop]

    def setProperty(self, prop, val):
        self.properties[prop] = val

    def printProperties(self):
        return self.properties
