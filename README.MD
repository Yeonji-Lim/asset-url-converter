이 프로젝트는 (주)달콤소프트 내에서 진행한 프로젝트로

허가를 받은 후 보안 관련 내용을 제외하고 복제하였습니다. (git mirror 사용)

- issue, pull request의 history는 삭제됨
- 보안 소스 파일이 필요하여 실제 실행 불가

# asset-url-converter

게임 데이터 파일의 CDN url 주소를 일괄 변경하는 프로젝트

## Requirements

- Python 3.9.7

## Quick Start

```
git clone https://github.com/dalcomsoft/asset-url-converter
cd asset-url-converter
pip install -r requirements.txt
```

에셋 파일 경로, 기존 CDN, 바뀔 CDN을 실행 인자로 입력하여 convert.py를 실행합니다.

```
python3 convert.py [게임 데이터 파일 경로] [기존 CDN] [바뀔 CDN]
```

예시 :

```
python3 convert.py test/data.xlsx 1234.cloudfront.net 5678.cloudfront.net
```

결과물은 입력한 에셋 엑셀의 위치에 `[입력한 에셋 엑셀의 이름]_converted_[실행날짜]_[실행시점].xlsx`로 생성됩니다.

예시 : `test/data_converted_20230217_155533.xlsx`
