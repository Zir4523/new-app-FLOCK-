## 本アプリ(FLOCK）へのアクセス  
***  
#### 次の記事より一部参照[Django girls](https://tutorial.djangogirls.org/ja/installation/)  
***  

#### アプリにアクセスするまでの工程  
1.pythonのインストール  
2.仮想環境の起動  
3.Djangoのインストール  
4.サーバーへアクセス  
***

#### 1.pythonのインストール  

以下のURLからpythonをダウンロードしてください。  
##### Windowsの場合  
https://www.python.org/downloads/windows/  
※自身のWindowsが32-bitか64-bitなのか確認してから該当するデータをダウンロードしてください。  

インストールの途中で、「Setup」というタイトルのウィンドウがでてきたら注意してください。 下にあるとおり、「Add Python 3.6 to PATH」か「Add Python to your environment variables」をチェックしてから「Install Now」をクリックしてください (バージョンが違うと表示が違うこともあります)。

##### Mac OSの場合  
https://www.python.org/downloads/release/python-361/  
※Mac OS X 64-bit/32-bit installer というファイルをダウンロードします。  
ダウンロードできたら python-3.6.1-macosx10.6.pkg をダブルクリックして実行します。

##### *コマンドウィンドウについて*

これからの操作はPCへの指示となるので、コマンドと言われる文字列の命令を実行していく必要があります。  
そのため、コマンドを入力・実行する場所を「コマンドウィンドウ」と言い、開きかたは次のとおりです。  
※  Windows・Mac OSにより違いがあるため、該当する方法で操作してください。  

#### Windowsの場合  
[Windows キー]+[R キー]を押すと[ファイル名を指定して実行]といウィンドウが立ち上がります。  
「cmd」と入力して[OK]をクリックしてください。  

#### Mac OSの場合  
[アプリケーション]→[ユーティリティ]→[ターミナル]を選択しましょう。  
***

#### 2.仮想環境の起動  

Djangoのインストールの前に仮想環境(virtual environment)の作成が必要です。  
なぜなら、仮想環境でどのようなことを試しても実際のサイト等には影響が出ないからです。  

コマンドラインは以下の通りです。  
```
python3 -m venv myvenv
```  
'myvenv'は自身の好きな文字列で良いです。  

・続いて起動に移ります。  

OSによって違うので、該当するコードを実行してください。  
##### Windowsの場合  
```
myvenv\Scripts\activate
```
##### Mac OSの場合
```
source myvenv/bin/activate
```
コンソールでプロンプトの行頭に (myvenv) が付いたら、仮想環境(virtualenv) を起動しています。  

#### 3.Djangoのインストール  
仮想環境が起動されたので、Djangoをインストールしてみましょう。  

コードは以下の通りです。  
```
python -m pip install --upgrade pip
```  

続いて'requirements.txt'をインストールしてください。  
```
pip install -r requirements.txt
```  
'requirements.txt'には以下のテキストがあります。  
```
Django~=3.2.10
```  
・'pip install -r requirements.txt'を実行することによって、Djangoをインストールできます。  

#### 4.サーバーへアクセス  

以下のコードを実行しアクセスしてください。  

```
python3 manage.py runserver
```
実行したら、URLが表示されるのでそれをクリックしてください。  

