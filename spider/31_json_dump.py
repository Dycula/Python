#示例一
import json
item={"name":"少年","card":"hello"}
with open("yt.json","a") as f:
    json.dump(item,f,ensure_ascii=False)

#json.load()把文件中的json串读取并转为pyhton数据类型
#with open("yt.json","r") as f:
#   result=json.load(f)
#print(type(result))


# 示例2
item_list = [
  {'name':'紫衫龙王','card':'123'},
  {'name':'青翼蝠王','card':'456'}
]
with open('ystlj.json','a') as f:
  json.dump(item_list,f,ensure_ascii=False)





