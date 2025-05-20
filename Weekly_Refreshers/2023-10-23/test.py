ls = ["ABOUT", "MONEY", "OTHER", "NOBLE", "GASOLINE", "UMBRELLA", "SENTIENCE"]

def subset(txt, uselessarg = None):
    if uselessarg is None:
        raise NotImplementedError
    return txt[0]

subbed = list(map(subset, ls))

print(subbed)