# Oriented_Bounding_Box  

バウンディングボックスには、AABB(Axis Aligned Bounding Box) と OBB(Orinented Bounding Box) に2種類がある。  

前者の方が計算が簡単でどのソフトにも実装されている（はず）。  

後者は実装されていない場合もあり、Grasshopper + OBB と検索すると、Galapagos の計算で解いてみよう！といった例を見つけることができる。  

そんなものは不要なので適切な実装を探す。Python では、Open3d のものと Trimesh のものがあり（多分、有名どことはこの辺）、Open3d は点群処理のイメージがあり、Trimesh は使っている人に便利よと聞いていたので。今回は Trimash を選択。  

[https://trimsh.org/index.html](https://trimsh.org/index.html)  


### OBB  

サンプルから、stl のロードの箇所を持ってきて、OBB 計算の関数を書いたら5行で何らかの箱できた。座標系が合ってないと思ったが、逆行列にしたら解決。数値は NumPy で計算されているので、Numpy の関数で導出。  


### Mesh-Boolean  

Trimesh はメッシュのブーリアン演算を備えているが、実際は Blender or OpenSCAD のカーネルを利用しているようだった。Blender にパスを通し、実際にメッシュのブーリアン演算ができた。  


### Ref  

[https://trimsh.org/index.html](https://trimsh.org/index.html)  

[Python, NumPyで行列の演算（逆行列、行列式、固有値など）](https://note.nkmk.me/python-numpy-matrix/)  

[Blenderをpythonでつくるためのセットアップ（Mac編）](https://asus4.hatenablog.com/entry/20090402/1238689738)  

