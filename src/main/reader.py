def read_input_data_from_file(input_file):
    try:
        with open(input_file, 'r') as file:
            lines = file.readlines()
            num_employers, num_kinds_of_beer = map(int, lines[0].split())

            if num_employers <= 0 or num_employers >= 50 or num_kinds_of_beer <= 0 or num_kinds_of_beer >= 50:
                return None

            strings = lines[1].split()

            if len(strings) != num_employers:
                return None

            for string in strings:
                if len(string) != num_kinds_of_beer:
                    return None

            return strings

    except FileNotFoundError:
        print(f"Error: File not found.")
        return None

    except Exception as e:
        print(f"Error: {e}")
        return None
