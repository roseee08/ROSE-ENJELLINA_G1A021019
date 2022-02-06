def pertama():
  print("=======================================")
  print("SELAMAT DATANG DI YOUFOOD ")
  print("=======================================")
  
  def welcome():
    print("\nApakah Anda Ingin Memesan Makanan Secara Online ? ")
    print("1.Ya" "\n2.Tidak")
    awal =input("\nPilihan Anda : ")
    if awal=="1" :
      print("\nSelamat Datang di Menu Pemesanan Makanan Online Youfood ")
    elif awal=="2":
      print("Anda Dapat Mengunjungi Toko Kami dan Memesan Secara Offline")
      quit()
    else:
      print("input yang anda masukkan salah")
      welcome()
  welcome()
  
  print('')
  Nama=input("Silahkan Masukkan Nama Anda:") 
  Kontak=int(input("Masukkan No HP/WA Anda:"))
 
  
  print("\nPILIHAN MENU")
  pilihan_menu=["1.MAKANAN","2.MINUMAN",]
  for menu1 in pilihan_menu:
    print(menu1,end="\n")

  def menu ():
    menu =int(input("MASUKAN PILIHAN ANDA :"))
    print("1.BAKSO\n","2.SATE\n","3.MIE AYAM\n",)
    menu =int(input("MASUKAN PILIHAN ANDA :"))
    if menu ==1:
      print("\nSELAMAT ANDA SUDAH MEMESAN MENU BAKSO")
    elif menu ==2:
      print("\nSELAMAT ANDA SUDAH MEMESAN MENU SATE")
    elif menu ==3:
      print("\nSELAMAT ANDA SUDAH MEMESAN MENU MIE AYAM")
    else:
      print("Silahkan Melakukan Pemesanan Ulang")
      menu ()
  menu ()
  
  print('')
  print("PILIHAN PAKET_MENU :")
  pilihan_paket=["1.HEMAT","2.KOMPLIT","3.GRUP"]
  for menu2 in pilihan_paket:
    print(menu2,end="\n")

  def paket ():
    Pilihan_paket=int(input("\nSilahkan Memasukkan Paket Pilihan Anda :"))
    if Pilihan_paket==1:
      print("=============================")
      print("Anda telah Memesan Paket Hemat")
      print("Silahkan Lanjutkan Proses Pemesanan")
      print("=============================")
    elif Pilihan_paket==2:
      print("===============================")
      print("Anda telah Memesan Paket Komplit")
      print("Silahkan Lanjutkan Proses Pemesanan")
      print("===============================")
    elif Pilihan_paket==3:
      print("===============================")
      print("Anda telah Memesan Paket Grup")
      print("Silahkan Lanjutkan Proses Pemesanan")
      print("===============================")
    else:
      print("Input yang anda masukkan salah")
      paket ()
  paket ()

  def last():
    print("")
    print("Silahkan Melakukan Proses Pembayaran")
    print("1.Ya \n2.Tidak")
    Again =input("\nPilihan Anda : ")
    if Again=="1":
      print("\n=======TERIMA KASIH TELAH MELAKUKAN PEMESANAN SECARA ONLINE=======")
      quit()
    elif Again=="2":
      pertama()
      
    else:
      print("input yang anda masukkan salah")
      last()
  last()

pertama()