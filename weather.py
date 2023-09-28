def main():
    weather_information = [
        {'prefecture': '東京都', 'station': '渋谷', 'temperature': 6.5},
        {'prefecture': '東京都', 'station': '池袋', 'temperature': 7.0},
        {'prefecture': '東京都', 'station': '新橋', 'temperature': 7.5},

        {'prefecture': '大阪府', 'station': '梅田', 'temperature': 8.2},
        {'prefecture': '大阪府', 'station': '大阪', 'temperature': 9.3},
        {'prefecture': '大阪府', 'station': '堺', 'temperature': 9.5},

        {'prefecture': '福岡県', 'station': '博多', 'temperature': 13.0},
        {'prefecture': '福岡県', 'station': '太宰府', 'temperature': 15.0},
    ]

def main():
    weather_information = [
        {'prefecture': '東京都', 'station': '渋谷', 'temperature': 6.5},
        {'prefecture': '東京都', 'station': '池袋', 'temperature': 7.0},
        {'prefecture': '東京都', 'station': '新橋', 'temperature': 7.5},

        {'prefecture': '大阪府', 'station': '梅田', 'temperature': 8.2},
        {'prefecture': '大阪府', 'station': '大阪', 'temperature': 9.3},
        {'prefecture': '大阪府', 'station': '堺', 'temperature': 9.5},

        {'prefecture': '福岡県', 'station': '博多', 'temperature': 13.0},
        {'prefecture': '福岡県', 'station': '太宰府', 'temperature': 15.0},
    ]

    # 全国の平均気温を計算
    total_temperature = sum(entry['temperature'] for entry in weather_information)
    average_temperature = total_temperature / len(weather_information)
    print(average_temperature)

    # 大阪府の駅名を取り出す
    osaka_stations = [entry['station'] for entry in weather_information if entry['prefecture'] == '大阪府']
    
    # カンマ区切りで出力
    print(', '.join(osaka_stations))


    fukuoka_temperatures = [entry['temperature'] for entry in weather_information if entry['prefecture'] == '福岡県']
    average_temperature_fukuoka = sum(fukuoka_temperatures) / len(fukuoka_temperatures)
    print(average_temperature_fukuoka)

if __name__ == '__main__':
    main()
