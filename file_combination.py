def compare_and_update_files(source_file, destination_file):
    with open(source_file, 'r') as src, open(destination_file, 'r+') as dest:
        src_lines = src.readlines()
        dest_lines = dest.readlines()
        
        # Convert destination lines to a set for faster lookup
        dest_set = set(line.strip() for line in dest_lines)
        
        for line in src_lines:
            stripped_line = line.strip()
            if stripped_line not in dest_set:
                dest.write('\n' + stripped_line)
                print(f"Added new record to destination file: {stripped_line}")
                dest_set.add(stripped_line)  # Add to set to avoid duplicates
        else:
            print("Both files contain the same records.")

# Example usage
source_file = r'./testFile1.txt' # change me
destination_file = r'./testFile2.txt' # change me
compare_and_update_files(source_file, destination_file)
