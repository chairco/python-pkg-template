# python-sample
Python package setting and sample

提供一個模板當在開發一個 Python Package 時可以快速套用，包含設定：

1. `setup.py` 的內容。
2. 開發套件內的檔案內容，例如 `/demo/demo.py`, `/demo/__init__.py` 內容。
3. 產生一份 `requirements.txt` 可以作為其他相依套件安裝。
4. 發佈時要 deploy 的內容 `MANIFEST` 設定。  
5. 測試採用 pytest, 因此包含 `setup.py` 與使用 tox 的測試參數 `tox.ini` 內容，包含產生測試涵蓋率。
6. Documentation 的文件。 

[詳細內容參考](http://www.infloop.tw/2015/01/11/building-your-own-python-project/)