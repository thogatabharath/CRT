arr=[2,2,2,4,4,4,3,3,10,1]
freq={}
for num in arr:
    freq[num]=freq.get(num,0)+1
maxi=max(freq,key=freq.get)
mini=min(freq,key=freq.get)
print("maximum frequncy number:",maxi)
print("minimum frequncy number:",mini)
