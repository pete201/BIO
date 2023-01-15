'''https://www.studytonight.com/python-howtos/how-to-generate-all-permutations-of-a-list'''

def perm(start, end=[], output=[]):
    #print(f' start={start}, end={end}')
    if(len(start) == 0):
        output.append(end)
    else:
        for i in range(len(start)):
            perm(start[:i] + start[i+1:], end + start[i:i+1])
    return output

#function call
print(perm([1,2,3]))

