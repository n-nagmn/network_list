import nmap
import sys

def network_scanner(network_prefix):
    """
    指定されたネットワークをスキャンし、デバイス、ポート、OSの情報を表示する関数
    """
    # NmapのPortScannerオブジェクトを作成
    nm = nmap.PortScanner()
    
    print(f"スキャンを開始します: {network_prefix}")
    print("デバイスの数やネットワークの状態によっては、数分かかることがあります...")

    try:
        # スキャンを実行
        # arguments='-O' はOS検出を有効にするオプション
        # sudo権限がないとOS検出は失敗することが多い
        nm.scan(hosts=network_prefix, arguments='-O -T5 --top-ports 100')
    except nmap.PortScannerError as e:
        print(f"Nmapスキャンエラー: {e}")
        print("Nmapがインストールされているか、またパスが通っているか確認してください。")
        print("OS検出には管理者権限（sudo）が必要な場合があります。")
        sys.exit(1)
    except Exception as e:
        print(f"予期せぬエラーが発生しました: {e}")
        sys.exit(1)

    print("\n--- スキャン結果 ---")

    # スキャン結果をホストごとに処理
    if not nm.all_hosts():
        print("アクティブなホストが見つかりませんでした。")
        return

    for host in nm.all_hosts():
        print("-" * 40)
        print(f"ホスト: {host} ({nm[host].hostname()})")
        
        # ホストの状態 (up or down)
        print(f"  状態: {nm[host].state()}")

        # OSの情報を表示
        if 'osmatch' in nm[host] and nm[host]['osmatch']:
            # 最も確度の高いOSを表示
            best_match = nm[host]['osmatch'][0]
            print(f"  OS推定: {best_match['name']} (確度: {best_match['accuracy']}%)")
        else:
            # sudoなしで実行した場合など、OS情報が取得できない場合
            print("  OS推定: 情報なし (管理者権限で実行すると取得できる可能性があります)")
        
        # プロトコルごとにポート情報を表示
        for proto in nm[host].all_protocols():
            print(f"  プロトコル: {proto}")
            
            ports = nm[host][proto].keys()
            sorted_ports = sorted(ports)
            
            if not sorted_ports:
                print("    開いているポートはありません。")
                continue

            for port in sorted_ports:
                port_info = nm[host][proto][port]
                print(f"    ポート: {port:<5}  状態: {port_info['state']:<10}  サービス: {port_info['name']}")
    
    print("-" * 40)
    print("\nスキャンが完了しました。")


if __name__ == '__main__':
    # スキャンしたいネットワーク範囲を指定
    # 例: '192.168.1.0/24', '192.168.1.1-100', 'localhost'
    # ご自身のネットワーク環境に合わせて変更してください。
    target_network = '' 

    # ユーザーに入力を求める場合
    # user_input = input(f"スキャン対象のネットワークを入力してください (デフォルト: {target_network}): ")
    # if user_input:
    #     target_network = user_input
    
    network_scanner(target_network)