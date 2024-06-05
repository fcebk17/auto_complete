# auto_complete
You can use this case to implement auto complete similar to google search.

## Use your own data to build the trie
### Step 1: Word segmentation (CKIP)
Modify the json filename in `segmented_word.py`, and run it
```
python segmented_word.py
```
### Step 2: Build and save the Trie
```
python save_trie.py
```
### Step 3: Packaged as an executable file
```
pyinstaller --onefile load_trie_and_search.py
```
### Step 4: Run
```
./dist/load_trie_and_search trie.pkl <keyword>
```

## Or you can use my trie :P
```
./dist/load_trie_and_search trie.pkl <keyword>
```
