# smart-novel-scrape-syosetukaninarou-lambda
小説家になろうの小説をスクレイピングする

## 設定  
| 項目 | 値 |  
| ---- | ---- |
| ランタイム | Python 3.8 |
| メモリ | 512 MB |
| タイムアウト | 5 s |
| layer | scrape_layer |

## 環境変数  
| 変数名 | 値 |  
| ---- | ---- |  
| API_ENDPOINT | https://api.syosetu.com/novelapi/api/ |  
| BASE_URL | https://ncode.syosetu.com/ |  
| SITE_NAME | syosetukaninarou |  