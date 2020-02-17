t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    ssum=n*(n+1)*(2*n+1)/6
    sums=(n*(n+1)/2)**2
    print sums-ssum
