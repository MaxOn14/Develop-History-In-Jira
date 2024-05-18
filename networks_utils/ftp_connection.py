import ftplib

source = 'source.txt'


def connection_to_server(server, username, password):
    try:
        ftp = ftplib.FTP(server)
        ftp.set_pasv(True)
        ftp.login(username, password)
        with open(source, 'wb') as local_file:
            ftp.retrbinary(f'RETR {source}', local_file.write())
    except ftplib.all_errors as e:
        print(f'Error is {e}')
    finally:
        if 'ftp' in locals():
            ftp.quit()


