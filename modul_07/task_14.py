def to_indexed(source_file, output_file):
    with open(source_file, 'r') as read_file:
        with open(output_file, 'w') as write_file:
            for i, line in enumerate(read_file):
                line_new = f"{i}: {line}"
                write_file.write(line_new)
                
                
to_indexed('modul_06//task_07_out.txt', 'modul_07//emploee.txt')