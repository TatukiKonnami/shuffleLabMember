# shuffleLabMember

CSVを読ませてなんとなく使えばランダムにソートする奴。

- Name : 名前
- Grade : 
  - B : 学部生
  - M : 修士
  - A : その他
- Organize : 幹事をやっていないか　
  - やっている-> 1　
  - やってない->2
  
### CSV Formatt  
``` test.csv

Name,Grade(B,M,A),Organize
Name,Grade(B,M,A),Organize
...

```

### 飲み会の幹事を決める
```
'what is the purpose?(Organize decision -> OD | Sort)
>> OD
```
やってない人がソートされて表示

### なんやかんやでランダムにソートする
```
'what is the purpose?(Organize decision -> OD | Sort)
>> Sort
```

```
'except grade (M, B, A)'
>> M A
```
並び替えないロールを選択（リストに含めないロールを選ぶ)

ソートされる

### お願い
適当に作ったので適当に修正とかなんやらPRお待ちしています

Autor Konnnami

dmb1703@stumail.daido-it.ac.jp



