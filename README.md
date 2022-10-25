# webp-compress

ディレクトリ内の画像を一括で WebP 形式に変換し、容量を落とすスクリプト。

この際、本来は欠損してしまうはずの EXIF データを JSON に書き出し、また Orientation 属性を基に画像を回転する。

一眼レフで撮影した 500 枚の画像に対して

- オリジナル（JPEG）：4.60 GB/500 枚
- 圧縮後（WebP + EXIF）：373 MB
- 圧縮率：7.9%

## 使い方
webp.py 内の base_dir（出力先ディレクトリ）を書き換える

directory 内の画像を一括で処理する

```
python webp.py <directory>
```
