def getAttribute(asset, name):
    return asset["data"]["article"][name]

def getStatus(asset,name):
    return asset["meta"]

def getAuthor(asset):
    return getAttribute(asset, "author")

def getDomain(asset):
    return getAttribute(asset, "domain")

def getSubDomain(asset):
    return getAttribute(asset, "subdomain")

def getDate(asset):
    return getAttribute(asset, "publish_date")

def getTitle(asset):
    return getAttribute(asset, "title")

def getLink(asset):
    return getAttribute(asset, "http")