'''
Program for converting the bounding boxes json file to labels in the kvasir-instrument dataset
'''
import json
import os

bboxes_path = "path_to_bboxes.json"
images_dir = "kvasir-instrument-without-pipe/images"
labels_dir = "kvasir-instrument-without-pipe/labels"

os.makedirs(labels_dir, exist_ok=True)

with open(bboxes_path) as f:
    bboxes = json.load(f)

for img_id, info in bboxes.items():
    h, w = info["height"], info["width"]
    label_path = os.path.join(labels_dir, f"{img_id}.txt")
    with open(label_path, "w") as out:
        for box in info["bbox"]:
            xmin, ymin, xmax, ymax = box["xmin"], box["ymin"], box["xmax"], box["ymax"]
            x_center = (xmin + xmax) / 2 / w
            y_center = (ymin + ymax) / 2 / h
            bw = (xmax - xmin) / w
            bh = (ymax - ymin) / h
            out.write(f"0 {x_center} {y_center} {bw} {bh}\n")
print("Conversion done.")