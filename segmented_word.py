import json
from ckip_transformers.nlp import CkipWordSegmenter

# 載入 filtered_data.json 檔案
with open('filtered_data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 初始化 CKIP 斷詞系統
ws_driver = CkipWordSegmenter(model="bert-base")

# 定義斷詞函數
def segment_text(text):
    result = ws_driver([text])
    return result[0]

# 儲存斷詞結果
segmented_results = []

# 只對前100筆資料進行斷詞
for item in data:
    segmented_content = segment_text(item['content'])
    segmented_results.append({'segmented_content': segmented_content})

# 將結果儲存至 segmented_data.json 檔案
with open('segmented_data.json', 'w', encoding='utf-8') as file:
    json.dump(segmented_results, file, ensure_ascii=False, indent=4)

print("資料斷詞完成，結果儲存在 segmented_data.json")
