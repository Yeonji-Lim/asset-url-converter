import sys
import re
from datetime import datetime
import pandas as pd

TARGET_ASSET_PATH = sys.argv[1]
OLD_CDN = sys.argv[2]
NEW_CDN = sys.argv[3]
OUTPUT_ASSET_PATH = '.'.join(TARGET_ASSET_PATH.split('.')[:-1]) + '_converted_' + str(datetime.now().strftime("%Y%m%d_%H%M%S")) + '.xlsx'

if len(sys.argv) != 4:
    print('실행 인자의 개수가 다릅니다.')
    sys.exit()

print('Asset file path : ' + TARGET_ASSET_PATH)
print('CDN : [ ' + OLD_CDN + ' ] convert to [ ' + NEW_CDN + ' ]')

print('Reading asset file...')
base_data_df = pd.read_excel(TARGET_ASSET_PATH, sheet_name=None, engine='openpyxl')

print('Preparing Writer...')
writer = pd.ExcelWriter(OUTPUT_ASSET_PATH, engine="openpyxl")

print('Start Converting...')
for key, df in base_data_df.items():
    df = df.replace(to_replace = OLD_CDN, value = NEW_CDN, regex=True)
    df = df.rename(columns= lambda x: re.sub('^Unnamed: [0-9]*', '', x))
    if key == 'CommonData':
        df.rename(columns={"code.1": "code"}, inplace=True)

    df.to_excel(writer, sheet_name=key, index=False)
    print('Converted Sheet : ' + key)

writer.save()
print('Convert Success!')
