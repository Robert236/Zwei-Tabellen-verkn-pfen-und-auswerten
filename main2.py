import copy
sorted_data = []
correct_data = []
incorrect_data = []
sorted_all_article = []

def print_datasets_out(data, outputfilename):
    with open(outputfilename, 'w') as OutputFile:
        for print_out in data:
            main_string = ''
            number = print_out['Artikel Nr.']
            main_string += number + ';'
            symbols = []
            for i, entry8 in enumerate(print_out['Format']):
                if i == 0:
                    main_string += entry8 + ';'
                else:
                    symbols.append(entry8)
            text = []
            for i, entry7 in enumerate(print_out['Text']):
                if i == 0:
                    main_string += entry7 + '\n'
                else:
                    text.append(entry7)
            to_print_sub_lines = []
            for line0 in symbols:
                ss = ';'
                ss += line0 + ';' + text.pop(0) + '\n'
                to_print_sub_lines.append(ss)
            OutputFile.write(main_string)
            for line2 in to_print_sub_lines:
                OutputFile.write(line2)


def read_data(filename):
    with open(filename, 'r') as InputFile:
        basic_container = {'Artikel Nr.': '', 'Format': [], 'Text': []}
        new_container = None
        for line in InputFile:
            line = line.replace('\n', '')
            line = line.split(';')
            if line[0].isdigit():
                if new_container is not None:
                    sorted_data.append(new_container)
                new_container = copy.deepcopy(basic_container)
                for key in new_container:
                    if key == 'Artikel Nr.':
                        new_container[key] = line.pop(0)
                    else:
                        new_container[key].append(line.pop(0))
            else:
                line.remove('')
                for key in new_container:
                    if key == 'Artikel Nr.':
                        pass
                    else:
                        new_container[key].append(line.pop(0))
        sorted_data.append(new_container)


read_data('Text_MATERIAL_GRUN_D neutralisiert.csv')
read_data('Text_MATERIAL_GRUN_E_neutralisiert.csv')

unique_numbers = []
for entry in sorted_data:
    unique_numbers.append(entry['Artikel Nr.'])
unique_list = list(dict.fromkeys(unique_numbers))

for entry2 in unique_list:  # es kommt erst der deutsch und danach der englische Text. ## Logik zum Thema!
    to_compare = []
    for entry3 in sorted_data:
        if entry3['Artikel Nr.'] == entry2:
            to_compare.append(entry3)
    for line in to_compare:
        sorted_all_article.append(line)
    if len(to_compare) == 2:
        descriptions = []
        for dic in to_compare:
            desc = ''
            for i, line in enumerate(dic['Text']):
                if i == 1:
                    desc += line
            if desc not in descriptions:
                descriptions.append(desc)
        if len(descriptions) == 2:
            for entry5 in to_compare:
                incorrect_data.append(entry5)
        else:
            for entry6 in to_compare:
                correct_data.append(entry6)
    else:
        for entry4 in to_compare:
            correct_data.append(entry4)


print_datasets_out(incorrect_data, 'output_incorrect_data.csv')
print_datasets_out(correct_data, 'output_correct_data.csv')
print_datasets_out(sorted_all_article, 'output_all_article_sorted.csv')
