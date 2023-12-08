import os
import csv

def get_directory_size(path):
    total_size_bytes = sum(os.path.getsize(os.path.join(dirpath, filename)) for dirpath, _, filenames in os.walk(path) for filename in filenames)
    total_size_kb = total_size_bytes / 1024.0  # Convert bytes to kilobytes
    return total_size_kb

def calculate_sizes(file_paths):
    sizes = []
    for path in file_paths:
        #path = path.replace('\\', '/')  # Comment this line if code not work
        if os.path.exists(path):
            
            parent_directory = os.path.dirname(path)
            size = get_directory_size(parent_directory)
            sizes.append((path, parent_directory, size))
        else:
            sizes.append((path, "Not Found"))
    return sizes

def write_to_csv(data, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['file paths', 'parent directory', 'Total size (KB)'])
        csv_writer.writerows(data)

def main(input_file, output_file):
    with open(input_file, 'r') as file:
        file_paths = file.read().splitlines()

    sizes = calculate_sizes(file_paths)
    write_to_csv(sizes, output_file)

if __name__ == "__main__":
    input_file_path = "file_paths.txt"  # Replace with your input file path
    output_file_path = "directory_sizes_kb.csv"  # you may change the output file as your choice

    main(input_file_path, output_file_path)
    print("Output file generated")
