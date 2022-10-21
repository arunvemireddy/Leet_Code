def repeatedString(s, n):
    # Write your code here
    news=s
    res=[]
    if len(s)==1 and 'a' in s:
        return n
    else:
        while True:
            if len(news)<n:
                news=news+s
            elif len(news)>n:
                news=news[:n]
                break
            elif len(news)==n:
                break
    
    for i in news:
        if i == 'a':
            res.append(i)
    
    return len(res)

print(repeatedString('kmretasscityylpdhuwjirnqimlkcgxubxmsxpypgzxtenweirknjtasxtvxemtwxuarabssvqdnktqadhyktagjxoanknhgilnm',736778906400))
