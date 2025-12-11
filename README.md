# Network Scanner (Python + Nmap)

PythonとNmapを使用して、指定したネットワーク内のアクティブなホスト、OS情報、および開いているポートをスキャンするツールです。

## 機能 (Features)

* **ホスト検出**: 指定したネットワーク範囲（CIDR形式）のアクティブなデバイスをリストアップします。
* **OS推定**: NmapのOS検出機能（`-O`）を使用して、稼働しているOSの種類とバージョンを推定します。
* **ポートスキャン**: 一般的な上位100ポートをスキャンし、開いているポートとサービス名を表示します。
* **ホスト名解決**: デバイスのホスト名を取得して表示します。

## 必要要件 (Requirements)

このツールを使用するには、Pythonライブラリだけでなく、**OSにNmap本体がインストールされている**必要があります。

* Python 3.x
* **Nmap** (コマンドラインツール)
* `python-nmap` (Pythonライブラリ)

## インストール (Installation)

### 1. Nmap本体のインストール

OSに合わせてNmapをインストールしてください。

* **Windows**: [Nmap公式サイト](https://nmap.org/download.html)からインストーラーをダウンロードしてインストールしてください。
* **macOS** (Homebrew):
    ```bash
    brew install nmap
    ```
* **Linux** (Ubuntu/Debian):
    ```bash
    sudo apt install nmap
    ```

### 2. Pythonライブラリのインストール

```bash
pip install python-nmap
````

## 🚀 使い方 (Usage)

### 1\. ネットワーク範囲の設定

`network_list.py` をエディタで開き、`target_network` 変数をご自身の環境に合わせて変更してください。

```python
if __name__ == '__main__':
    # 例: '192.168.1.0/24' (一般的な家庭内LAN)
    target_network = '192.168.200.0/24' 
```

### 2\. スクリプトの実行

OS検出（`-O`オプション）を行うため、\*\*管理者権限（sudo または 管理者として実行）\*\*での実行を推奨します。権限がない場合、OS情報は取得できません。

**Linux / macOS:**

```bash
sudo python network_list.py
```

**Windows:**
コマンドプロンプトまたはPowerShellを「管理者として実行」し、以下のコマンドを入力します。

```cmd
python network_list.py
```

## 出力例 (Output Example)

```text
スキャンを開始します: 192.168.200.0/24
デバイスの数やネットワークの状態によっては、数分かかることがあります...

--- スキャン結果 ---
----------------------------------------
ホスト: 192.168.200.1 (router.local)
  状態: up
  OS推定: Linux 4.x (確度: 98%)
  プロトコル: tcp
    ポート: 80     状態: open        サービス: http
    ポート: 443    状態: open        サービス: https
----------------------------------------
ホスト: 192.168.200.15 (desktop-pc)
  状態: up
  OS推定: Microsoft Windows 10 (確度: 96%)
  プロトコル: tcp
    ポート: 135    状態: open        サービス: msrpc
    ポート: 445    状態: open        サービス: microsoft-ds
----------------------------------------

スキャンが完了しました。
```

## 免責事項 (Disclaimer)

このツールは、**自分が管理しているネットワーク、または管理者の許可を得たネットワーク**でのみ使用してください。許可なく他人のネットワークをスキャンする行為は、不正アクセス禁止法などの法律に抵触する恐れがあります。開発者は、このツールの使用によって生じたいかなる損害についても責任を負いません。

## License

MIT License