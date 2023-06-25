


def main(parse_file):
    fp = open(parse_file, "r")
    header = fp.readline().strip().split("\t")

    print(header)
    print(len(header))

    rest_contents = fp.read()
    fp.close()

    x = 0
    count = 0
    description_seen = False
    row = []
    my_results_dict = []
    while(x < len(rest_contents)):

        # if count %7 and rest_contents[0] == '\r':
        if description_seen: #post description, now parse until seee new lien
            new_offset = rest_contents.find("\n", x)
            if new_offset == -1:
                token = rest_contents[x:]
                new_offset = len(rest_contents)
            else:
                token = rest_contents[x:new_offset]
            row.extend(token.split("\t"))
            description_seen = False
            count = -1

            gap = len(header) - len(row)
            row = row + [""] * gap
            print(dict(zip(header, row)))
            my_results_dict.append(dict(zip(header, row)))
            #print(" --- ".join(row))
            row = []

        else:
            if count == 3: #description, grab it
                description_seen = True
                new_offset = rest_contents.index('\t', x)
                token = rest_contents[x:new_offset]
                token = token.replace("\n", " | ")
                row.append(token)

            else: #description not seen
                new_offset = rest_contents.index('\t', x)
                token = rest_contents[x:new_offset]
                row.append(token)




        x = new_offset + 1
        count = count + 1
    return my_results_dict, header




if "__main__" in __name__:
    csv_res, csv_header = main("BankParseExample")

    import csv
    fw = open("output.csv", "w", newline="")
    dic_writer = csv.DictWriter(fw, fieldnames=csv_header)
    dic_writer.writeheader()
    dic_writer.writerows(csv_res)
    fw.close()
