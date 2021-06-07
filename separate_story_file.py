import os

directory = r'ML_Final_Processed_Data'
separator = ''

for filename in os.listdir(directory):
    count = 0
    with open("ML_Final_Processed_Data/" + filename, "r", encoding="utf-8") as f:
        new_story = []
        for line in f:
            if not line.startswith("@highlight"):
                new_story.append(line)
            if line.startswith("@highlight"):
                count = count +1
                if count == 1:
                    new_story.append(line)
                elif count == 2:
                    base = os.path.splitext(filename)[0]
                    new_file_name =  base + '.story'
                    with open(f"single_sum_stories/{new_file_name}", "w", encoding="utf-8") as f:
                        f.write(separator.join(new_story))
                    new_story.append(line)
                elif count == 3:
                    base = os.path.splitext(filename)[0]
                    new_file_name =  base + '.story'
                    with open(f"double_sum_stories/{new_file_name}", "w", encoding="utf-8") as f:
                        f.write(separator.join(new_story))
                    new_story.append(line)
        with open(f"triple_sum_stories/{new_file_name}", "w", encoding="utf-8") as f:
            f.write(separator.join(new_story))

            
