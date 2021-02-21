output = []
count = 0

strings = ['ab', 'abc', 'dfg', 'ab']
queries = ['ab', 'df', 'dfg']

for i in range(len(queries)):
    for j in range(len(strings)):
        if queries[i] == strings[j]:
            count += 1
            print(count)

print(output)