import json
import os

FILE_NAME = 'daftar_kontak.json'

def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            return json.load(file)    
    else:
        print('File tidak terbaca')
    
    return[]

def save_data(daftar_kontak):
    with open(FILE_NAME, 'w') as file:
        json.dump(daftar_kontak, file, indent=4)


def display_daftar_kontak(no, kontak):
        '''untuk buat display kontak'''
        print(f"{f'Daftar kontak no - {no}':^50}")    
        print(f"\nNama \t\t\t: {kontak['nama']}")
        print(f"Email\t\t\t: {kontak['email']}")
        print(f"Telepon\t\t\t: {kontak['telepon']}")
        print(50*'-')


def function_daftar_kontak (daftar_kontak):
    '''untuk melihat daftar kontak yang ada'''
    for no, kontak in enumerate (daftar_kontak, start=1):  
        display_daftar_kontak(no, kontak)      
        

def function_tambah_kontak(daftar_kontak):
    '''untuk menambahkan kontak'''
    while True:
        nama = input('Nama\t: ')
        email = input('Email\t: ')
        telepon = input('Telepon\t: ')
        print(50*'-')
        
        kontak = {
            'nama': nama,
            'email': email,
            'telepon': telepon
        }

        daftar_kontak.append(kontak)
        save_data(daftar_kontak) # untuk simpan data kontak ke file json
        
        is_done = input('Apakah ingin lanjut tambah kontak (y/n) : ').lower()
        print(50*'-')
        if is_done == 'n':
            break
        elif is_done == 'y':
            pass
        else:
            print('Input tidak valid, masukan y/n')


def function_cari_kontak(daftar_kontak):
    '''untuk mencari kontak'''
    while True:
        keyword_cari = input('Masukan Nama / Telepon / Email yang dicari : ').lower()
        print(50*'-')
        ketemu = False

        for no, kontak in enumerate (daftar_kontak, start=1):
            if (keyword_cari in kontak['nama'].lower() 
                or keyword_cari in kontak['email'].lower()
                or keyword_cari in kontak['telepon'].lower()):
                display_daftar_kontak(no, kontak)
                ketemu = True
        
        if not ketemu:
            print('Tidak ditemukan kontak')
            print(50*'-')
        
        is_done = input('Apakah ingin lanjut mencari (y/n) : ').lower()
       
        if is_done == 'n':
            print(50*'-')
            break
        elif is_done == 'y':
            pass
        else:
            print('Input tidak valid, masukan y/n')
        
        print(50*'-')


def function_delete_kontak(daftar_kontak):
    '''untuk menghapus kontak'''
    while True:
        
        keyword_delete = input('Masukan Nama / Telepon / Email yang ingin dihapus : ')
        print(50*'-')
        ketemu = False

        for no, kontak in enumerate(daftar_kontak, start=1):
            if (keyword_delete == kontak['nama'] 
                or keyword_delete == kontak['email']
                or keyword_delete == kontak['telepon']):
                
                display_daftar_kontak(no, kontak)
                while True:
                    input_konfirmasi_delete = input('Apakah ingin menghapus data di atas : ').lower()
                    print(50*'-')
                    if input_konfirmasi_delete == 'y':
                        daftar_kontak.remove(kontak)
                        save_data(daftar_kontak)
                        ketemu = True
                        print(f'Kontak dengan nama : {kontak['nama']}, berhasil dihapus')
                        print(50*'-')
                        break
                    elif input_konfirmasi_delete == 'n':
                        print('Penghapusan dibatalkan!')
                        break
                    else:
                        print('Input tidak valid, masukan y/n')

        
        if not ketemu:
            print('Tidak ada di daftar kontak')
            print(50*'-')

        is_done = input('Apakah ingin lanjut mendelete (y/n) : ').lower()
       
        if is_done == 'n':
            print(50*'-')
            break
        elif is_done == 'y':
            pass
        else:
            print('Input tidak valid, masukan y/n')
        
        print(50*'-')