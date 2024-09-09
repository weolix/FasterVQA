label = r"examplar_data_labels/LSVQ/labels_test.txt"
import os
i = 0
with open(label, 'r') as f:
    lines = f.readlines()
    for line in lines:
        if not os.path.exists("/home/user/XUX/datasets/LSVQ/videos/"+line.strip().split(',')[0]):
            print(line.strip().split(',')[0])
            i += 1
    if i == 0:
        print("All files exist.")
