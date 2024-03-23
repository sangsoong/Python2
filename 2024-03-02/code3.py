import json

dic = {
    "이름": "XXX",
    "나이": 19,
    "학교정보": {
        "학교" : "XX고등학교",
        "학번" : 30900
    }
}

print(json.dumps(dic, ensure_ascii=False, indent=5))