def hash_function(obj):
    pre_temp_1 = []
    for i in range(0, len(obj) // 2):
        pre_temp_1.append(f'ord(obj[{i}]) * ord(obj[-{i + 1}])')
    str_temp_1 = ' + '.join(pre_temp_1) if len(obj) % 2 == 0 else ' + '.join((pre_temp_1[:-1] + [pre_temp_1[-1].split(' * ')[0]]))
    temp_1 = eval(str_temp_1)
    pre_temp_2 = []
    signs = ''.join(['-+' for i in range(len(obj))])
    for i, sign in zip(range(0, len(obj) - 1), signs):
        pre_temp_2.append(f'ord(obj[{i}]) * {i + 1} {sign} ')
    temp_2 = ''.join(pre_temp_2)[:-3]
