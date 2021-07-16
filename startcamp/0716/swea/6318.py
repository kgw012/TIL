data_str = 'abcdef'
num_range = range(0, 6)

data_dict = dict(zip(data_str, num_range))

for k, v in data_dict.items():
    print(f"{k}: {v}")