from typing import Dict, List
from datetime import date, datetime

from pydantic import BaseModel, validator

class NovelModel(BaseModel):
    key: str = None
    title: str = None
    url: str = None
    site_name: str = None
    author: str = None
    description: str = None
    created_at: float = None
    updated_time: float = None
    genre: str = None
    tag: List[str] = None
    length: int = None
    like_count: int = None
    pv: int = None
    contents: str = None
    sys_created_at: float = None

dic_genre = {
    101: "異世界",
    102: "現実世界",
    201: "ハイファンタジー", 
    202: "ローファンタジー", 
    301: "純文学", 
    302: "ヒューマンドラマ", 
    303: "歴史", 
    304: "推理", 
    305: "ホラー", 
    306: "アクション",
    307: "コメディー", 
    401: "VRゲーム", 
    402: "宇宙", 
    403: "空想科学",
    404: "パニック", 
    9901: "童話",
    9902: "詩", 
    9903: "エッセイ",
    9904: "リプレイ",
    9999: "その他", 
    9801: "ノンジャンル"
}


if __name__ == "__main__":
    pass