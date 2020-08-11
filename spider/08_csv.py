import csv
with open ("test.csv","w",newline="") as f:
    writer=csv.writer(f)
    writer.writerow(["步惊云","30"])
    writer.writerow(["小哥哥","25"])
#writerows([(),(),()])
with open ("test.csv","w",newline="") as f:
    writer=csv.writer(f)
    writer.writerows([("少年","30"),("哥哥","24"),("小姐姐","23")])