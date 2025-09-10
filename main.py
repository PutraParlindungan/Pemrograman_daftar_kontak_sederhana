import os
import function

daftar_kontak = function.load_data()

if __name__ == '__main__':
    while True:
        os_name = os.name
        match os_name:
            case 'posix': 
                os.system('clear')
            case 'nt': 
                os.system('cls')
        
        print(50*'=')
        print(f"{'MANAGEMENT KONTAK':^50}") 
        print(50*'=')

        print('1. Daftar Kontak')
        print('2. Tambah Kontak')
        print('3. Cari Kontak')
        print('4. Hapus Kontak')
        print('5. Exit')

        print(50*'-')
        input_option = input('Masukan pilihan opsi : ')
        print(50*'-')

        match input_option:
            case '1':
                print('\n'+50*'=')
                print(f"{'DAFTAR KONTAK':^50}")
                print(50*'=')
                function.function_daftar_kontak(daftar_kontak)

            case '2':
                print('\n'+50*'=')
                print(f"{'TAMBAH KONTAK':^50}")
                print(50*'=')
                function.function_tambah_kontak(daftar_kontak)

            case '3':
                print('\n'+50*'=')
                print(f"{'CARI KONTAK':^50}")
                print(50*'=')
                function.function_cari_kontak(daftar_kontak)
            case '4':
                print('\n'+50*'=')
                print(f"{'DELETE KONTAK':^50}")
                print(50*'=')
                function.function_delete_kontak(daftar_kontak)
            case '5':
                break
        
            case _:
                print('TIDAK ADA OPSI')

        is_done = input('Apakah ingin lanjut pilih opsi menu (y/n) : ')
        print(50*'-')
        if is_done == 'n':
            break

    print(f"{'PROGRAM SELESAI':^50}")
    print(50*'=')