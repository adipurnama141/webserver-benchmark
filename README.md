# Analisis Kinerja Web Server

Oleh  : Adi Purnama / 13514006


## Tool Benchmarking

Tool benchmark yang digunakan adalah ltest (ltest.py). 
Tool ini dikembangkan sendiri menggunakan Python.
Berfungsi untuk mengukur waktu respons rata rata suatu web server terhadap
simulasi 10.000 request konkuren suatu resource.

Sementara itu, Windows Task Manager digunakan untuk mengukur memory yang digunakan oleh web 
server saat menangani request.


## Cara Melakukan Test

1. Buat file html dummy , berukuran 20kb dan 500 bytes.
2. Nyalakan web server, pastikan kedua file tersebut dapat diakses via web server.
3. Atur konfigurasi pada ltest.py, masukan URL resource tersebut.
4. Run ltest.py 
5. Ltest akan menampilkan waktu respon rata-rata.
6. Buka Windows Task Manager, lihat kolom "Peak Working Set (Memory)" untuk melihat memori yang digunakan oleh web server

## Hasil Test

1.	Apache , 20 KB
	30 KB Memory
	0,01790 s
	
2. 	Apache, 500 B
	27 KB Memory
	0,01439 s
	
3. 	Nginx, 20 KB
	5 KB Memory
	Tes gagal, hanya 2137 request tertangani.
	Berikut adalah waktu yang dibutuhkan, untuk menangani n request.
	Dimana n < 10.000
	1 request	: 	1.03 s
	10 request	: 	1.097 s
	100 request	: 	1.23 s
	1000 request:	1.606 s
	
4. 	Nginx, 500 B
	5 KB Memory
	1,10217 s