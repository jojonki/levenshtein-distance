# Leven Shtein (Edit Distance)

## Installation (if you use word mode in Japanese)
```
$ pip install -r requirements.txt
```

## How to use Levenshtein program
```
$ python main.py --strA おはようございます --strB おはこんにちは  --verbose 1
  ['-', 'お', 'は', 'よ', 'う', 'ご', 'ざ', 'い', 'ま', 'す']
  - [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  - お [1, 0, 1, 2, 3, 4, 5, 6, 7, 8]
  - は [2, 1, 0, 1, 2, 3, 4, 5, 6, 7]
  - こ [3, 2, 1, 1, 2, 3, 4, 5, 6, 7]
  - ん [4, 3, 2, 2, 2, 3, 4, 5, 6, 7]
  - に [5, 4, 3, 3, 3, 3, 4, 5, 6, 7]
  - ち [6, 5, 4, 4, 4, 4, 4, 5, 6, 7]
  - は [7, 6, 5, 5, 5, 5, 5, 5, 6, 7]
  - Edit distance: 0.7777777777777778

$ python main.py --strA おはようございます --strB おはこんにちは --mode word --verbose 1
  ['-', 'おはよう', 'ござい', 'ます']
  - [0, 1, 2, 3]
  - お [1, 1, 2, 3]
  - は [2, 2, 2, 3]
  - こんにちは [3, 3, 3, 3]
  - Edit distance: 1.0
```

