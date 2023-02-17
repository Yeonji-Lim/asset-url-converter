# asset-url-converter

에셋 엑셀 파일의 CDN url 주소를 일괄 변경하는 프로젝트

# Requirements

- Python 3.9.7

# Quick Start

```
git clone https://github.com/dalcomsoft/asset-url-converter
cd asset-url-converter
pip install -r requirements.txt
```

에셋 파일 경로, 기존 CDN, 바뀔 CDN을 실행 인자로 입력하여 convert.py를 실행합니다.

```
python3 convert.py [에셋 파일 경로] [기존 CDN] [바뀔 CDN]
```

예시 :

```
python3 convert.py test/SSM_Live_3.7.23_230215.xlsx d13i7sjdvvio90.cloudfront.net d1mg6lluotuboq.cloudfront.net
```

결과물은 입력한 에셋 엑셀의 위치에 `[입력한 에셋 엑셀의 이름]_converted_[실행날짜]_[실행시점].xlsx`로 생성됩니다.

예시 : `test/SSM_Live_3723_230215_converted_20230217_155533.xlsx`
