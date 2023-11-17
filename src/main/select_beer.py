from src.main.reader import read_input_data_from_file
from src.main.writer import write_results_to_file


def graph_with_read_data(input_file):
    data_list = read_input_data_from_file(input_file)
    if not data_list:
        return None

    graph = {}

    for data_index, value in enumerate(data_list):
        graph[data_index] = []
        for index, char in enumerate(value):
            if char == 'Y':
                graph[data_index].append(index)
    return graph


def select_kinds_of_beer(input_file, file_to_result):
    graph_employers = graph_with_read_data(input_file)
    if not graph_employers:
        return "Incorrect input data"

    processed_employers = []
    selected_beer = []
    graph_employers = dict(sorted(graph_employers.items(), key=lambda x: len(x[1])))
    for employer, kinds_of_beer in graph_employers.items():

        if set(selected_beer).intersection(kinds_of_beer):
            processed_employers.append(employer)
            continue

        if employer not in processed_employers and kinds_of_beer[0] not in selected_beer:
            selected_beer.append(kinds_of_beer[0])
            processed_employers.append(employer)

    write_results_to_file(len(selected_beer), file_to_result)
    return len(selected_beer)
