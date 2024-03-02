import pickle


with open('dict_list.csv', 'r', encoding='utf-8') as f:
    data = []
    for line in f:
        key, value = line.strip().split(',')
        data.append({key: value})
print(pickle.dumps(data))

