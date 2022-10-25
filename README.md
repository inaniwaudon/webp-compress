# webp-compress

ディレクトリ内の画像を一括で WebP 形式に変換し、容量を落とすスクリプト。  
この際、本来は欠損してしまうはずの EXIF データを JSON に書き出し、また Orientation 属性を基に画像を回転する。

## 使い方
webp.py 内の base_dir（出力先ディレクトリ）を書き換える

directory 内の画像を一括で処理する

```
python webp.py <directory>
```
