#Filtering datos2007.csv by obras

with open('data/datos2007.csv', 'r') as f_in:
    with open('data/datos2007filt.csv', 'w') as f_out:
        lines = f_in.readlines()
        for i in range(len(lines)):
            if "Obras" in lines[i]:
                f_out.write(lines[i])


with open('data/datos2007filt.csv', 'r') as f_in:
    with open('out/datos2007_latlon.csv', 'w') as f_out:
        lines = f_in.readlines()
        for i in range(len(lines)):
            lines_split = lines[i].split(";")
            tmp_line = lines_split[2] + ";" + lines_split[-1]
            f_out.write(tmp_line)
