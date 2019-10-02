def cleanStringWithSample(str):
    if("sample#" in str): 
        return str.replace("sample#","") 
    else: 
        return str

def convertStringToDict(content):
    ouptutDictResult = {}
    row = content.split(" ")
    for col in row:
        key = cleanStringWithSample(col.split("=")[0])
        value = cleanStringWithSample(col.split("=")[1])
        ouptutDictResult[key] = value

    return ouptutDictResult