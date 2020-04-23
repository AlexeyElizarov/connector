def ndict(lst):
    """
    Returns a nested dict from a list with last item as a value.
    https://stackoverflow.com/questions/7653726/how-to-turn-a-list-into-nested-dict-in-python
    :param lst: list to nested dict
    :return: nested dict
    """

    nested_dict = {}

    for path in lst:
        current_level = nested_dict
        for i in range(len(path[:-2])):
            part = path[i]
            if part not in current_level:
                if i == len(path[:-2]) - 1:
                    current_level[part] = {path[-2]: eval(path[-1])}
                else:
                    current_level[part] = {}
            current_level = current_level[part]

    return nested_dict
