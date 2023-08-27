## 本アプリ(FLOCK）へのアクセス  
***  
#### 次の記事より一部参照[Django girls](https://tutorial.djangogirls.org/ja/installation/)  
***  

#### アプリにアクセスするまでの工程  
1.gitbashのインストール  
2.pythonのインストール  
3.仮想環境の起動  
4.Djangoのインストール  
5.サーバーへアクセス  
***

#### 1.git bashのインストール  

まずこのリポジトリからデータをダウンロードするにあたってgit bashが必要になります。  
以下のURLからOSに合ったgitbashをインストールしてください。  
（今後の操作はgit bashで行います。） ※Windowsの方は注意してください。 
https://gitforwindows.org/  

次に適当なところにフォルダを作成し、データをダウロードしてください。  
方法はいくつかありますが、その一つとして以下のコードを実行してください。  
```
git clone url
```  
※urlはこのリポジトリのコードからURLをコピーして使用してください。  
***  

#### 2.pythonのインストール  

以下のURLからpythonをダウンロードしてください。  
##### Windowsの場合  
https://www.python.org/downloads/windows/  
※自身のWindowsが32-bitか64-bitなのか確認してから該当するデータをダウンロードしてください。  
追記：必要に応じてMicrosoft　storeからpythonのアプリをダウンロードしてください。  

##### Mac OSの場合  
https://www.python.org/downloads/release/python-361/  
※Mac OS X 64-bit/32-bit installer というファイルをダウンロードします。  
***

#### 3.仮想環境の起動  

Djangoのインストールの前に仮想環境(virtual environment)の作成が必要です。  
なぜなら、仮想環境でどのようなことを試しても実際のサイト等には影響が出ないからです。  

コマンドラインは以下の通りです。  
```
python -m venv myvenv
```  
'myvenv'は自身の好きな文字列で良いです。  
※特に何も起こりませんが大丈夫です。  

・続いて起動に移ります。  

##### git bash 及びMac OSの場合の操作は
```
source myvenv/bin/activate
```
コンソールでプロンプトの行頭に (myvenv) が付いたら、仮想環境(virtualenv) を起動しています。  
***
#### 4.Djangoのインストール  
仮想環境が起動されたので、Djangoをインストールしてみましょう。  

コードは以下の通りです。  
```
python -m pip install --upgrade pip
```  
※upgrade pipは同時にアップデートもしてくれる方法

続いて'requirements.txt'をインストールしてください。  
```
pip install -r requirements.txt
```  
・'pip install -r requirements.txt'を実行することによって、Djangoをインストールできます。  
***
#### 5.サーバーへアクセス  

サーバーへアクセスする前にデータをmigrate（適用させる）必要があります。  
以下のコードを実行してください。  
```
python manage.py migrate
```
※色んな表示が出ますが基本はokと表示されるはずなので、大丈夫です。  

最後に以下のコードを実行しアクセスしてください。  

```
python manage.py runserver
```
実行したら、URLが表示されるのでそれをコピーしてブラウザ等でペーストしてください。    

