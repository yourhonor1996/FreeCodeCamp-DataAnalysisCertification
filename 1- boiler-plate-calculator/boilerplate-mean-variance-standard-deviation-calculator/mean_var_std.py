import numpy as np

def calculate(inp:list):

    if len(inp) < 9:
        raise ValueError('List must contain nine numbers.')

    calculations = {}
    matrix = np.reshape(inp,(3,3))

    # Initialize the dictionary containing the initial items and their values (which are lists)
    what_to_calc = ['mean', 'variance', 'standard deviation', 'max', 'min', 'sum']
    for what in what_to_calc:
        calculations.update({what:[]})
    
    axi = [0, 1]
    # for each axis append the measurments to the dicionary
    for ax in axi:    
        calculations['mean'].append(list(matrix.mean(axis = ax)))
        calculations['variance'].append(list(matrix.var(axis = ax)))
        calculations['standard deviation'].append(list(matrix.std(axis = ax)))
        calculations['max'].append(list(matrix.max(axis = ax)))
        calculations['min'].append(list(matrix.min(axis = ax)))
        calculations['sum'].append(list(matrix.sum(axis = ax)))
    # since the last is not an iterable (and cannot be passed to the list command)
    # we have to append it seperately
    calculations['mean'].append(matrix.mean())
    calculations['variance'].append(matrix.var())
    calculations['standard deviation'].append(matrix.std())
    calculations['max'].append(matrix.max())
    calculations['min'].append(matrix.min())
    calculations['sum'].append(matrix.sum())
    
    return calculations



# a = np.array([1,2,3,4,5,6,7,8,9]).reshape((3,3))
# print(calculate([1,2,3,4,5,6,7,8,9]))
# # print(a[0:3][0:1])
# a.me

# # print(type(a))