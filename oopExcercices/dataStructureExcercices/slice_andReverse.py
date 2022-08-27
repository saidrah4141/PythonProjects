'''
Created on Aug. 26, 2022

*Slice list into 3 equal chunks and reverse each chunk

@author: Said
'''

sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]


length = len(sample_list)
chunk_size = int(length / 3)
start = 0
end = chunk_size


for i in range(3):
    list1 = sample_list[slice(start,end)]
    print("chunk", list1)
    print("reverse", list(reversed(list1)))
    start= end
    end+=chunk_size
    
