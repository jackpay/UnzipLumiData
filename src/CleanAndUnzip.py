__author__ = 'jack'

import os,zlib,datetime

def cleanFile(file,outLoc,size=1):
    f = open(file,'rb')
    f.read(size)
    data = f.read()
    ungzippedFile = zlib.decompressobj().decompress(data)
    out = open(outLoc + '/' + os.path.basename(file),'wb')
    out.write(ungzippedFile)
    out.close()
    f.close()

def processFiles(fileDir,outLoc,size=1):
    print("Processing files...")
    start = datetime.datetime.utcnow()
    i = 0
    for f in os.listdir(fileDir):
        try :
            cleanFile(fileDir + "/" + f,outLoc,size)
        except :
            print("Failed on file: " + str(i) + " Name: " + f)
            pass
        i += 1
    finish = datetime.datetime.now() - start
    print("Processed " + str(i) + " files in " + str(finish.total_seconds()) + " seconds")

if __name__ == "__main__":
    fileDir = '/home/jack/Documents/Projects/Lumi/lumi-data'
    outDir = '/home/jack/Documents/Projects/Lumi/unzippedDocs'
    size = 1
    processFiles(fileDir,outDir,size)

