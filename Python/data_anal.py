import json

with open("data.json", encoding="utf-8") as datafile:
    air_data = json.load(datafile)["DATA"]



gu_numbr = {"도봉구" : 15, "동대문구" : 17, "동작구" : 18, "은평구":37, "강북구":4, "강동구":2, "강서구":5, "금천구":12,
            "구로구": 10, "관악구":7, "광진구":9, "강남구" :0, '종로구': 41, '중구':42, '중랑구':43, '마포구':20, '노원구':14,
            '서초구':25, '서대문구':23, '성북구':27, '성동구':26, '송파구':29, '양천구':32, '영등포구':33, '용산구' : 36}

for key, value in gu_numbr.items():
    sum = 0
    count = 0
    for i in range(295):
        data_index = 50*i + value
        pm10_data = air_data[data_index]['pm10']
        if pm10_data != None:
            sum+= pm10_data
            count+=1

        else:
            pass

    print(key + " : " + str(sum/count))
    count = 0
