# -*- coding: utf-8 -*-
# author lby
from elasticsearch7 import Elasticsearch

es = Elasticsearch([{"host": "admin", "port": 9200}])

body = {
     "query": { # 查询命令
         # "match_phrase"，只模糊匹配，不分词
         "match": { # 查询方法：模糊查询（会被分词）。比如此代码，会查到只包含：“我爱你”， “中国”的内容
         "v_name": "综艺 1"
         }
     }
}

# body1，项目中搜索引擎需要使用的查询
body1 = {
     'from': 0, # 相当于 mysql 的 limit 的偏移量，从 0 开始
     "size": 20, # 相当于 limit 的步长
     "query": { # 查询命令
         "bool": {
             "should": [
                 {
                     "match": {
                     "v_name": "搜索"
                     }
                 },
                 {
                     "match": {
                     "director": "导演"
                     }
                 },
                 {
                     "match": { "leading_players": "演员"
                     }
                 }
             ]
         }
     },
     "sort": { # 对满足条件的数据排序
     "id": { # 根据 id 字段排序
         "order": "asc" # asc 升序，desc 降序
         }
     }
}


# index参数对应jdbc.conf里面的output的index => "t_video_info"
res = es.search(index="t_video_info", body=body1)

print(res)

# 未来使用es查询数据，得到这个data，就要的结果集
data = res["hits"]["hits"]

for row in data:
    print(row)
