def any_word_list(word_list, string):
    any_in_list = False
    for word in word_list:
        if word in string:
            any_in_list = True
    return any_in_list


def combination_in_label(word_lists, string):
    any_all_in_list = False
    for word_list in word_lists:
        all_in_list = True
        for word in word_list:
            if word not in string:
                all_in_list = False
        any_all_in_list = (any_all_in_list or all_in_list)
    return any_all_in_list


# loading labels as 2D list of strings
label_list = []
label_file_read = open('../data/rawData/labels/ngcLabels.txt', 'r')
for i, line in enumerate(label_file_read):
    items = line.split(' ; NGC ')
    label_list.append([])
    for j in range(len(items) - 1, -1, -1):
        label_list[i].append(items[j].lower())
    label_list[i].append("NA")

label_file_read.close()

# transforming ngc id into int
for i in range(len(label_list)):
    object_number = label_list[i][0]
    label_list[i][0] = int(object_number[: len(object_number) - 2])


# assigning each object to a simplified label
for i in range(len(label_list)):
    if any_word_list(["galaxy", "galaxies", "blazar", "quasar"],
                     label_list[i][1]):
        label_list[i][2] = "galaxy"
    if combination_in_label([["open", "cluster"],
                             ["cluster", "stars"],
                             ["association of stars"]], label_list[i][1]):
        label_list[i][2] = "open cluster"
    if combination_in_label([["double", "star"]], label_list[i][1]):
        label_list[i][2] = "multiple star"
    if "planetary nebula" in label_list[i][1]:
        label_list[i][2] = "planetary nebula"
    if "globular cluster" in label_list[i][1]:
        label_list[i][2] = "globular cluster"
    if "hii (ionized) region" in label_list[i][1]:
        label_list[i][2] = "nebula"
    if "reflection nebula" in label_list[i][1]:
        label_list[i][2] = "nebula"
    if "interstellar matter" in label_list[i][1]:
        label_list[i][2] = "nebula"
    if "emission object" in label_list[i][1]:
        label_list[i][2] = "nebula"
    if "supernova remnant" in label_list[i][1]:
        label_list[i][2] = "nebula"
    if "galactic nebula" in label_list[i][1]:
        label_list[i][2] = "nebula"


ignored_objects = []
for i in range(len(label_list)):
    if label_list[i][2] == "NA":
        ignored_objects.append([label_list[i][0], label_list[i][1]])
print("NGC id, Object label")
for object in ignored_objects:
    print(object)

print("total NA", len(ignored_objects))


label_file_write = open('../data/cleanedLabels/labels.txt', 'w')
for i in range(len(label_list)):
    if label_list[i][2] != "NA":
        label_file_write.write(
            str(label_list[i][0]) + ";" +
            str(label_list[i][1]) + ";" +
            str(label_list[i][2]) + "\n")
label_file_write.close()
