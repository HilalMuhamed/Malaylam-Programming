class CodeGen:
    
    def __init__(s,fullPath):
        s.fullPath = fullPath
        s.header=""
        s.code = []
    
    def gen(s,code):
        s.code.append(code) 
    def genLine(s,code):
        s.code.append(code + '\n')
    
    def headerLine(s,code):
        s.header += code +'\n'
    
    def writeFile(s):
        with open(s.fullPath,'w', encoding="utf-8") as outPutFile:
            outPutFile.write(s.header + ''.join(s.code) )
    