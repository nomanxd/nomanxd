import sys
import os
import hashlib 


def sha1(path, blocksize = 65536):
    afile = open(path, 'rb')
    h = hashlib.sha1()
    buf = afile.read(blocksize)
    while len(buf) > 0:
        h.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return h.hexdigest()
    
    
def findDup(direct):
    duplikates = {}
    for dirName, _, fileList in os.walk(direct):
        for filename in fileList:
            path = os.path.join(dirName, filename)
            cur = sha1(path)
            if cur not in duplikates:
                duplikates[cur] = []
            duplikates[cur].append(path)
    for _, lst in duplikates.items():
        if(len(lst) > 1):
            print(':'.join(lst)) 
    return 
    
    
if __name__ == '__main__':
    findDub(sys.argv[1])
    
