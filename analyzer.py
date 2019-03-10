

def analyze(page_as_string, list_of_names):
    result_map = {}
    for name in list_of_names:
        count = page_as_string.lower().count(name)
        result_map[name] = count
    return result_map
