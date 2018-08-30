



def tanimoto(query, target):
    nc = 0
    for query_byte, target_byte in zip(query, target):
        if query_byte == target_byte ==1:
            nc += 1
    na = query.count(1)
    nb = target.count(1)
    return nc/(na+nb-nc)

def check_insoluble(solubility):
    """
    solubility = solubility dataframe row
    :param solubility:
    :return:
    """
    p = []
    for c, ROW in enumerate(solubility):
        if list(ROW) == [1, 0]:
            p.append(c)
    return p