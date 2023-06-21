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
label_file_read = open('data/rawData/labels/ngcLabels.txt', 'r')
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

# Counting each class
sum_labels = {
    "galaxy": 0,
    "open_cluster": 0,
    "multiple_star": 0,
    "planetary_nebula": 0,
    "globular_cluster": 0,
    "nebula": 0,
    "NA": 0
}

# assigning each object to a simplified label
for i in range(len(label_list)):
    if any_word_list(["galaxy", "galaxies", "blazar", "quasar"],
                     label_list[i][1]):
        label_list[i][2] = "galaxy"
        sum_labels["galaxy"] += 1
    elif combination_in_label([["open", "cluster"],
                               ["cluster", "stars"],
                               ["association of stars"]], label_list[i][1]):
        label_list[i][2] = "open_cluster"
        sum_labels["open_cluster"] += 1
    elif combination_in_label([["double", "star"]], label_list[i][1]):
        label_list[i][2] = "multiple_star"
        sum_labels["multiple_star"] += 1
    elif "planetary nebula" in label_list[i][1]:
        label_list[i][2] = "planetary_nebula"
        sum_labels["planetary_nebula"] += 1
    elif "globular cluster" in label_list[i][1]:
        label_list[i][2] = "globular_cluster"
        sum_labels["globular_cluster"] += 1
    elif "hii (ionized) region" in label_list[i][1]:
        label_list[i][2] = "nebula"
        sum_labels["nebula"] += 1
    elif "reflection nebula" in label_list[i][1]:
        label_list[i][2] = "nebula"
        sum_labels["nebula"] += 1
    elif "interstellar matter" in label_list[i][1]:
        label_list[i][2] = "nebula"
        sum_labels["nebula"] += 1
    elif "emission object" in label_list[i][1]:
        label_list[i][2] = "nebula"
        sum_labels["nebula"] += 1
    elif "supernova remnant" in label_list[i][1]:
        label_list[i][2] = "nebula"
        sum_labels["nebula"] += 1
    elif "galactic nebula" in label_list[i][1]:
        label_list[i][2] = "nebula"
        sum_labels["nebula"] += 1
    else:
        label_list[i][2] = "NA"
        sum_labels["NA"] += 1

print("Label summary:")
for label, count in sum_labels.items():
    print(f"{label}: {count} ({round(100 * count / len(label_list), 2)}%)")

ignored_objects = []
for i in range(len(label_list)):
    if label_list[i][2] == "NA":
        ignored_objects.append([label_list[i][0], label_list[i][1]])
print("\nNA values:\nNGC id, Object label")
for object in ignored_objects:
    print(object)


label_file_write = open('data/cleanedLabels/labels.txt', 'w')
for i in range(len(label_list)):
    if label_list[i][2] != "NA":
        label_file_write.write(
            str(label_list[i][0]) + ";" +
            str(label_list[i][1]) + ";" +
            str(label_list[i][2]) + "\n")
label_file_write.close()
