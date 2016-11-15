def recurCount (to, curr, by):
    if curr > to:
        return to
    else:
        print (curr)
        return recurCount (to, curr+by, by)
recurCount(to, curr+by, by)
