def count_freqencies(arr):
    freq={}
    for num in arr:
        freq[num]=freq.get(num,0)+1
    return freq
arr=[1,2,3,4,4,3,2,1,1,1,2,2,3,3,4,4]
freqencies = count_freqencies(arr)
for i,count in freqencies.items():
    print(i,count)