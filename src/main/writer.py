def write_results_to_file(result, file_name):
    try:
        if not file_name:
            return 0
        with open(file_name, 'w+') as file:
            string_to_write = f"We have to buy {result} kinds of beer to avoid offending anyone"

            if result == "Incorrect input data":
                string_to_write = "Incorrect input data"
            file.write(string_to_write)
        print(f"Results written to file successfully.")
    except IOError as e:
        print(f"Error writing to file: {e}")
