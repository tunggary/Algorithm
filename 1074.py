import sys
sys.setrecursionlimit(100000)
n, r, c = map(int, sys.stdin.readline().split())

n = int(2**n)

def dfs(len,row,col,count):
  global r,c
  if len == 1:
    if row == r and col == c:
      print(count)
  else:
    half = len//2
    halfSquare = (len//2)**2
    if row+half > r and col+half > c:
      dfs(half,row,col,count)
    if row+half > r and col+half <= c:
      dfs(half,row,col+half,count+halfSquare)
    if row+half <= r and col+half > c:
      dfs(half,row+half,col,count+halfSquare*2)
    if row+half <= r and col+half <= c:
      dfs(half,row+half,col+half,count+halfSquare*3)
    
dfs(n,0,0,0)
    