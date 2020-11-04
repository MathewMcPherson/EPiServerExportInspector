import xml.etree.ElementTree as ET

class XmlWorker:
    def __init__(self, _filePath):
        self.filePath = _filePath
        self.parsedXml = self.parseXml()

    def parseXml(self):
        return ET.parse(self.filePath)
    
    def getItemNames(self):
        pages = self.parsedXml.getroot()[1]
        pageNames = []
        for page in pages:
            pageProperties = page[0][1]
            for prop in pageProperties:
                if prop[9].text == "PageName":
                    pageNames.append(prop[10].text)
        pages2 = self.parsedXml.getroot()[2]
        for page2 in pages2:
            pageProperties = page2[0][1]
            for prop in pageProperties:
                if prop[9].text == "PageName":
                    pageNames.append(prop[10].text)
        return pageNames

    def getTotalTimesHomeExported(self):
        pages = self.getItemNames()
        count = 0
        for page in pages:
            if page == "Home":
                count+=1
        return count
        

