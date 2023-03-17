# webp-compress

ディレクトリ内の画像を一括で WebP 形式に変換し、容量を落とすスクリプトです。

この際、本来は欠損してしまうはずの EXIF データを JSON に書き出し、また Orientation 属性を基に画像を回転します。

本スクリプトを実行した結果、一眼レフで撮影した 500 枚の画像に対して、以下の効果が得られました。

- オリジナル（JPEG）：4.60 GB/500 枚
- 圧縮後（JPEG + EXIF）：373 MB
- 圧縮率：7.9%

## 使い方

org_dir 内の画像を一括で処理し、dst_dir 以下に書き出す

```
python webp.py org_dir dst_dir [from_index]
```
