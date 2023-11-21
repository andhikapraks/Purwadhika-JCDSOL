#-------------------------------------- DATABASE KARYAWAN PERUSAHAAN ABCD -------------------------------------#
DatabaseKaryawan = [
  {
    "Nomor Karyawan": 101,
    "Name": "Arnie",
    "Gender": "Female",
    "Age": "20",
    "Department": "Human Resource",
    "Level": "Staff",
    "Status": "Part time"
  },
  {
    "Nomor Karyawan": 102,
    "Name": "Bryan",
    "Gender": "Male  ",
    "Age": "25",
    "Department": "Finance",
    "Level": "Staff",
    "Status": "Full time"
  },
  {
    "Nomor Karyawan": 103,
    "Name": "Charles",
    "Gender": "Male  ",
    "Age": "28",
    "Department": "Marketing",
    "Level": "Staff",
    "Status": "Full time"
  },
  {
    "Nomor Karyawan": 104,
    "Name": "Daphne",
    "Gender": "Female",
    "Age": "41",
    "Department": "Marketing",
    "Level": "Head",
    "Status": "Full time"
  },
  {
    "Nomor Karyawan": 105,
    "Name": "Eureka",
    "Gender": "Female",
    "Age": "30",
    "Department": "Legal",
    "Level": "Manager",
    "Status": "Full time"
  },
  {
    "Nomor Karyawan": 106,
    "Name": "Franco",
    "Gender": "Male  ",
    "Age": "30",
    "Department": "Marketing",
    "Level": "Manager",
    "Status": "Full time"
  }
]

# ************ (KARYAWAN - READ DATA *****************
def ReadDataKaryawan ():
    print('''
------------------------------------------------------------
|      Silahkan pilih action yang ingin Anda lakukan:      |
|                                                          |
|  1) Melihat data diri saya                               |
|  2) Kembali ke menu awal                                 |
|                                                          |
------------------------------------------------------------''')
    while True:
        PilihanMenuKaryawan= input("Silakan pilih menu (1/2): ")
        while PilihanMenuKaryawan == '1':
            InputNomorKaryawan = input("\nSilakan masukkan Nomor Karyawan Anda: ")
            DataCheck = None
            for i in DatabaseKaryawan:
                if str(i["Nomor Karyawan"]) == InputNomorKaryawan:
                    DataCheck = i
                
            if DataCheck is None:
                print ("\n ***MOHON MAAF DATA TIDAK DITEMUKAN. COBA LAGI!***")
                ReadDataKaryawan()
            else:
                print(f'''\n====BERIKUT DATA KARYAWAN ANDA SAAT INI==== \n Nomor Karyawan: {DataCheck['Nomor Karyawan']} \n Name: {DataCheck['Name']} \n Gender: {DataCheck['Gender']} \n Age: {DataCheck['Age']} \n Department: {DataCheck['Department']} \n Level: {DataCheck['Level']} \n Status: {DataCheck['Status']}''')
                ReadDataKaryawan()
        while PilihanMenuKaryawan == '2':
            MainMenuGeneral()
        else:
            print("\n****PILIHAN TIDAK TERIDENTIFIKASI. COBA LAGI!****")
            ReadDataKaryawan()
      
# # ************ (ADMIN - READ DATA) *****************
def ReadDataAdmin():
    print('''
------------------------------------------------------------
|      Silahkan pilih action yang ingin Anda lakukan:      |
|                                                          |
|  1) Melihat data seluruh karyawan                        |
|  2) Melihat data satu karyawan                           |
|  3) Kembali ke menu awal                                 |
|                                                          |
------------------------------------------------------------''')
    while True:
        PilihanMenuAdmin= input("Silakan pilih menu (1/2/3): ")
        while PilihanMenuAdmin == '1':
            if len(DatabaseKaryawan) == 0:
                print ("***DATABASE TIDAK DITEMUKAN!***")
                ReadDataAdmin ()
            else:
                print('\t\t==== BERIKUT ADALAH DATA SELURUH KARYAWAN PERUSAHAAN ABCD ====')
                print('---------------------------------------------------------------------------------------------------------------------')
                print('| ID| Name  \t\t| Gender \t| Age\t| Department\t\t| Level\t| Status\t|')
                print('---------------------------------------------------------------------------------------------------------------------')
                for i in DatabaseKaryawan:
                    print(f"| {i['Nomor Karyawan']:3}\t| {i['Name']:<16}| {i['Gender']:<8}| {i['Age']}\t| {i['Department']:<20}| {i['Level']}\t| {i['Status']}\t|")
                ReadDataAdmin ()
        while PilihanMenuAdmin == '2':
            InputNomorKaryawan = input("\nSilakan masukkan Nomor Karyawan yang ingin dicari: ")
            DataCheck = None
            for i in DatabaseKaryawan:
                if str(i["Nomor Karyawan"]) == InputNomorKaryawan:
                    DataCheck = i
            if DataCheck == None:
                print ("\n ***MOHON MAAF DATA TIDAK DITEMUKAN. COBA LAGI!***")
                ReadDataAdmin ()
            else:
                print(f'''\n====BERIKUT DATA KARYAWAN YANG ANDA CARI==== \n Nomor Karyawan: {DataCheck['Nomor Karyawan']} \n Name: {DataCheck['Name']} \n Gender: {DataCheck['Gender']}  \n Age: {DataCheck['Age']} \n Department: {DataCheck['Department']} \n Level: {DataCheck['Level']} \n Status: {DataCheck['Status']}''')
                ReadDataAdmin()
        while PilihanMenuAdmin == '3':
            MainMenuAdmin()
        else:
            print("\n****PILIHAN TIDAK TERIDENTIFIKASI. COBA LAGI!****")
            ReadDataAdmin ()

# ************ (ADMIN - CREATE/ADD DATA) *****************
def CreateDataAdmin():
    print('''
------------------------------------------------------------
|      Silahkan pilih action yang ingin Anda lakukan:      |
|                                                          |
|  1) Tambah data karyawan baru                            |
|  2) Keluar                                               |
|                                                          |
------------------------------------------------------------''')
    while True:
        PilihanMenuAdmin= input("Silakan pilih menu (1/2): ")

        while PilihanMenuAdmin == '1':
            NomorKaryawanBaru = input("Masukkan nomor karyawan baru yang ingin ditambahkan: ")
            if NomorKaryawanBaru.isnumeric() == True:
                DataCheck = None
                for i in DatabaseKaryawan:
                    if str(i["Nomor Karyawan"]) == NomorKaryawanBaru:
                        DataCheck = i
                        
                if DataCheck is not None:
                    print ("\n ***MOHON MAAF DATA DENGAN NOMOR KARYWAN INI SUDAH ADA. COBA LAGI!***")
                    CreateDataAdmin()
                else:
                    DataKaryawanBaru = {}
                    DataKaryawanBaru["Nomor Karyawan"] = NomorKaryawanBaru
                    DataKaryawanBaru["Name"] = input("Masukkan nama: ")
                    DataKaryawanBaru["Gender"] = input("Masukkan jenis kelamin: ")
                    DataKaryawanBaru["Age"] = input("Masukkan umur: ")
                    DataKaryawanBaru["Department"] = input("Masukkan departemen: ")
                    DataKaryawanBaru["Level"] = input("Masukkan level jabatan: ")
                    DataKaryawanBaru["Status"] = input("Masukkan status karyawan: ")
                
                    while True:
                        KonfirmasiTambahanData = input("Apakah Anda yakin ingin menambahkan database karyawan ini (Y/N)? ").upper()
                        if KonfirmasiTambahanData == 'Y':
                            DatabaseKaryawan.append(DataKaryawanBaru)
                            print ("\n***Data karyawan baru sudah ditambahkan. Database telah terupdate***")
                            CreateDataAdmin()
                        elif KonfirmasiTambahanData == 'N':
                            print("\n***Data karyawan baru tidak jadi ditambahkan ke dalam database***")
                            CreateDataAdmin()
                        else:
                            print("\n****PILIHAN TIDAK TERIDENTIFIKASI. COBA LAGI!****")
            else:
                print("\n****PILIHAN TIDAK TERIDENTIFIKASI. COBA LAGI!****")
                CreateDataAdmin()
        while PilihanMenuAdmin == '2':
            MainMenuAdmin()
        else:
            print("\n****PILIHAN TIDAK TERIDENTIFIKASI. COBA LAGI!****")
            CreateDataAdmin()
                
# ************ (ADMIN - UPDATE DATA) *****************
def UpdateDataAdmin():
    print('''
------------------------------------------------------------
|      Silahkan pilih action yang ingin Anda lakukan:      |
|                                                          |
|  1) Mengubah/memperbaharui data karyawan                 |
|  2) Keluar                                               |
|                                                          |
------------------------------------------------------------''')
    while True:
        PilihanMenuAdmin= input("Silakan pilih menu (1/2): ")
        while PilihanMenuAdmin == '1':
            InputNomorKaryawan = input("\nSilakan masukkan Nomor Karyawan yang datanya ingin Anda ubah/perbaharui: ")
            
            DataCheck = None
            for i in DatabaseKaryawan:
                if str(i["Nomor Karyawan"]) == InputNomorKaryawan:
                    DataCheck = i
            
            if DataCheck is None:
                print ("\n***DATA YANG DICARI TIDAK TERSEDIA. MOHON COBA LAGI***")
                UpdateDataAdmin()
            else:
                print (f"\n***BERHASIL MENEMUKAN DATABASE DENGAN NOMOR KARYAWAN {InputNomorKaryawan} YANG INGIN DIUBAH.***")
                barisUntukDiupdate = None
                indexUntukDiupdate = None
                nomorIndexUntukDiupdate = int(input('''\nSilakan masukkan data point apa yang datanya ingin Anda ubah/perbaharui: \n 1) Nomor Karyawan \n 2) Name \n 3) Gender \n 4) Age \n 5) Department \n 6) Level \n 7) Status \n Pilih antara (1 - 7)? '''))
                match nomorIndexUntukDiupdate:
                    case 1:
                        indexUntukDiupdate = "Nomor Karyawan"
                    case 2:
                        indexUntukDiupdate = "Name"
                    case 3:
                        indexUntukDiupdate = "Gender"   
                    case 4:
                        indexUntukDiupdate = "Age"
                    case 5:
                        indexUntukDiupdate = "Department"
                    case 6:
                        indexUntukDiupdate = "Level"
                    case 7:
                        indexUntukDiupdate = "Status"    
                print (f"\nAnda akan mengubah data {indexUntukDiupdate.upper()} dari karyawan {InputNomorKaryawan:3}\t")
                print (f"\nValue saat ini: {i[indexUntukDiupdate]:3}\t")
                barisUntukDiupdate = i
                i[indexUntukDiupdate] = input("\nValue baru:")
                print(f"\n***DATA BERHASIL DIUBAH***. \nValue saat ini: {i[indexUntukDiupdate]:3}\t")
                print(f'''\n====BERIKUT DATA KARYAWAN YANG TELAH DIUPDATE==== \n Nomor Karyawan: {i['Nomor Karyawan']} \n Name: {i['Name']} \n Gender: {i['Gender']}  \n Age: {i['Age']} \n Department: {i['Department']} \n Level: {i['Level']} \n Status: {i['Status']}''')
                CreateDataAdmin()
        while PilihanMenuAdmin == '2':
            MainMenuAdmin()
        else:
            print("\n****PILIHAN TIDAK TERIDENTIFIKASI. COBA LAGI!****")
            UpdateDataAdmin()
      
# ************ (ADMIN - DELETE DATA) *****************

def DeleteDataAdmin ():
    print('''
------------------------------------------------------------
|      Silahkan pilih action yang ingin Anda lakukan:      |
|                                                          |
|  1) Menghapus salah satu data karyawan                   |
|  2) Menghapus seluruh data karyawan                      |
|  3) Kembali ke menu awal                                 |
|                                                          |
------------------------------------------------------------''')
    while True:
        PilihanMenuAdmin= input("Silakan pilih menu (1/2/3): ")
        while PilihanMenuAdmin == '1':
            InputNomorKaryawan = (input("\nSilakan masukkan Nomor Karyawan yang datanya ingin Anda hapus: "))
            DataCheck = None
            for i in DatabaseKaryawan:
                if str(i["Nomor Karyawan"]) == InputNomorKaryawan:
                    DataCheck = i
            if DataCheck == None:
                print ("\n ***MOHON MAAF DATA TIDAK DITEMUKAN. COBA LAGI!***")
                DeleteDataAdmin()
            else:
                HapusData = input(f"Apakah Anda yakin ingin menghapus data Karyawan {DataCheck['Name']} (Y/N)? ").upper()
                if HapusData == 'Y':
                    IndexToDelete = DatabaseKaryawan.index(DataCheck)
                    del DatabaseKaryawan[IndexToDelete]
                    print ('''\n***PENGHAPUSAN DATA TELAH BERHASIL***\n\n =====Data karyawan terkini=====''')
                    print('---------------------------------------------------------------------------------------------------------------------')
                    print('| ID| Name  \t\t| Gender \t| Age\t| Department\t\t| Level\t| Status\t|')
                    print('---------------------------------------------------------------------------------------------------------------------')
                    for i in DatabaseKaryawan:
                        print(f"| {i['Nomor Karyawan']:3}\t| {i['Name']:<16}| {i['Gender']:<8}| {i['Age']}\t| {i['Department']:<20}| {i['Level']}\t| {i['Status']}\t|")
                    DeleteDataAdmin()
                elif HapusData =='N':
                    print ("Data tidak jadi dihapus. Program akan kembali ke halaman menu sebelumnya")
                    DeleteDataAdmin()
                else: 
                    print("\n****PILIHAN TIDAK TERIDENTIFIKASI. COBA LAGI!****")
        while PilihanMenuAdmin == '2':
            HapusData = input(f"Apakah Anda yakin ingin menghapus seluruh data Karyawan (Y/N)? ").upper()
            if HapusData == 'Y':
                del DatabaseKaryawan[0:]
                print ('''\n***PENGHAPUSAN DATA TELAH BERHASIL***\n\n \t\t =====Data karyawan terkini=====''')
                print('---------------------------------------------------------------------------------------------------------------------')
                print('| ID| Name  \t\t| Gender \t| Age\t| Department\t\t| Level\t| Status\t|')
                print('---------------------------------------------------------------------------------------------------------------------')
                for i in DatabaseKaryawan:
                    print(f"| {i['Nomor Karyawan']:3}\t| {i['Name']:<16}| {i['Gender']:<8}| {i['Age']}\t| {i['Department']:<20}| {i['Level']}\t| {i['Status']}\t|")
                DeleteDataAdmin()
            elif HapusData =='N':
                print ("Data tidak jadi dihapus. Program akan kembali ke halaman menu sebelumnya")
                DeleteDataAdmin()
            else:
                print("\n****PILIHAN TIDAK TERIDENTIFIKASI. COBA LAGI!****")
        while PilihanMenuAdmin == '3':
            MainMenuAdmin()
        else:
            print("\n****PILIHAN TIDAK TERIDENTIFIKASI. COBA LAGI!****")
            DeleteDataAdmin()
            
# ************ (ALL - EXIT PROGRAM) *****************
def ExitProgram ():
    global StatusMainMenu
    print('''\nTerima kasih telah mengunjungi database karyawan perusahaan ABCD''')
    StatusMainMenu = False

# ************ MAIN MENU *****************
def MainMenuAdmin():        
    UserIDAdmin = '1234'
    global StatusMainMenu
    while StatusMainMenu == True:
        UserIDInput = input ('Masukkan User ID Anda: ')
        if UserIDInput == UserIDAdmin:
            print ('''
------------------------------------------------------------
|      Silahkan pilih action yang ingin Anda lakukan:      |
|                                                          |
|  1) Menampilkan Daftar Karyawan                          |
|  2) Menambah Daftar Karyawan                             |
|  3) Mengubah Daftar Karyawan                             |
|  4) Menghapus Daftar Karyawan                            |
|  5) Keluar                                               |
|                                                          |
------------------------------------------------------------''')
            PilihanMenu = input("Silakan pilih menu yang ingin diakses (1-5): ")
            if PilihanMenu == '1':
                ReadDataAdmin()
            elif PilihanMenu == '2':
                CreateDataAdmin ()
            elif PilihanMenu == '3':
                UpdateDataAdmin ()
            elif PilihanMenu == '4':
                DeleteDataAdmin ()
            elif PilihanMenu == '5':
                MainMenuGeneral ()
            else: print ("\n****PILIHAN TIDAK TERIDENTIFIKASI. COBA LAGI!****")
        elif UserIDInput != UserIDAdmin:
            print ('''Mohon maaf ID yang Anda input salah''');
            while StatusMainMenu == True:
                PilihanMenu = input("Apakah Anda ingin ulangi? (Y/N): ").upper()
                if PilihanMenu == "Y":
                    MainMenuAdmin()
                elif PilihanMenu == "N": 
                    MainMenuGeneral()
                else: print ("\n****PILIHAN TIDAK TERIDENTIFIKASI. COBA LAGI!****")

def MainMenuGeneral():
    global StatusMainMenu
    while StatusMainMenu:
        print ('''
------------------------------------------------------------
|      Selamat datang di database karyawan PT. ABCD        |
|          Silahkan pilih akses yang Anda miliki:          |
|                                                          |
|  1) Admin                                                |
|  2) Karyawan                                             |
|  3) Keluar Database                                      |
|                                                          |
------------------------------------------------------------''')
        PilihanMenu = input("Masuk sebagai (1/2/3): ")
        if  PilihanMenu == '1':
            MainMenuAdmin()
        elif  PilihanMenu == '2':
            ReadDataKaryawan()
        elif PilihanMenu == '3':
            ExitProgram ()
        else: 
            print("\n****PILIHAN TIDAK TERIDENTIFIKASI. COBA LAGI!****")

StatusMainMenu = True
MainMenuGeneral()