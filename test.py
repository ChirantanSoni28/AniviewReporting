def reporttype():
    dimension = ['iid','iname','pcid','pcidName']
    metric = ['inventory','request','impression','revenue','cost','profit']
    character = ['%2C','&']

    for l in range(len(dimension)):
        dimension = dimension + character
        print(dimension)

print(reporttype())