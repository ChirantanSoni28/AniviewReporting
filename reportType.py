import sys

def reporttype():

    report_type = sys.argv[1]
    global dim, met

    dimension = ['daily','iid','iname','pcid','pcidName',"ncidName","aid","nasidName"]
    metric = ['inventory','request','impression','revenue','cost','profit',"bid","AdLoaded"]
    character = ['%2C','&']

    if report_type == "PublisherReport":

        dim = "dimensions="+ dimension[0] + character[0] + dimension[1] + character[0] + dimension[2] + character[0]  \
              + dimension[3] + character[0]  + dimension[4] + character[0]  + dimension[5] + character[1]

        met = "metrics=" + metric[0] + character[0] + metric[1] + character[0] + metric[2] + character[0] + \
              metric[3] + character[0] + metric[4] + character[0] + metric[5] + character[1]


    elif report_type == "Adsource Report":

        dim = "dimensions=" + dimension[0] + character[0] + dimension[1] + character[0] + dimension[3] + character[0] \
              + dimension[4] + character[0] + dimension[6] + character[0] + dimension[7] + character[1]

        met = "metrics=" + metric[0] + character[0] + metric[1] + character[0] + metric[2] + character[0] + metric[3] \
              + character[0] + metric[4] + character[0] + metric[5] + character[1]

    elif report_type == "Waterfall Optimization":

        dim = "dimensions=" + dimension[0] + character[0] + dimension[1] + character[0] + dimension[3] + character[0] \
              + dimension[6] + character[0] + dimension[7] + character[1]

        met = "metrics=" + metric[0] + character[0] + metric[1] + character[0] + metric[2] + character[0] + metric[6] \
              + character[0] + metric[7] + character[1]


    fileFormat = "format=json&"
    query = "%7B%7D"

    fields = dim + met + fileFormat + query

    return fields

# print(reporttype())