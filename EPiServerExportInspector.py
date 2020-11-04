from Workers.XmlWorker import XmlWorker

def main():
    xml = XmlWorker("epix.xml")
    for page in xml.getItemNames():
        print(page)
    print("Home exported: ", xml.getTotalTimesHomeExported())

main()