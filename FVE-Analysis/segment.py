input_file = 'Corrected.gfg'
output_file = 'Corrected2.gfg'
delimiter = '\t'  # You can change the delimiter to any character you prefer

with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
    for line in f_in:
        line = line.strip()
        values = line.split()
        fixed_line = delimiter.join(values)
        f_out.write(fixed_line + '\n')

print('Segmentation fixed. Fixed data saved in', output_file)
