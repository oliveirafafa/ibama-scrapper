from app.ibama_download_manager import IbamaDownloadManager


def main():
    im = IbamaDownloadManager()
    im.get_arrecadacao_data()
    im.get_multa_data()


if __name__ == '__main__':
    main()
