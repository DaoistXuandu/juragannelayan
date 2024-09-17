URL KE PWS: https://raihan-akbar-juaragannelayan.pbp.cs.ui.ac.id/


# Tugas 2
### **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**


Untuk bisa melakukan berbagai operasi yang demikian pertama masuk dalam suatu virtual enviroment untuk mengunduh dan membuat tempat dalam pengembanan web dengan menggunakan perintah `pip install -r requirements.txt` yang mana requirements.txt merupakan _file_ yang berisi list _package_ yang harus diunduh dalam menjalankan suatu proyek django saya menggunakan perintah `django-admin startproject -nama project- .` yang mana merupakan perintah default untuk menyusun struktur utama suatu aplikasi berbasis django. lalu untuk dapat menyusun susunan web yang rapi saya membuat suatu _folder_ dengan nama _main_ yang mana berisi aplikasi utama dari django, dimana didapatkan dengan menggunakan perintah `python manage.py startapp main`. Lalu untuk membuat struktur pada web, saya membuat suatu _folder_ bernama _template_ yang berisi suatu _file_ bernama main.html yang mana struktur html dari web django ini. Lalu untuk bisa mengaplikasikan MVT data dibuat menjadi tidak statis dengan memanggil variabel `app_name`, `name` dan `class`. 


Lalu agar data pada variabel yang akan dipanggil pada main.html maka kita perlu membuat definisi masing-masing variabel tersebut dengan membuat suatu fungsi bernama `show_main` pada views.py yang mana mendefinisikan nilai `app_name`, `name`, dan `class`, lalu mengembalikkan solusi dengan secara spesifik menuju pada laman main.html, lalu agar aplikasi dapat terimplementasi dengan baik kita harus melakukan proses _routing_ dan pemberian hak akses pada beberapa hal. Pertama agar _folder_ main dapat digunakan maka kita perlu memasukkan `main` pada `INSTALLED_APPS` pada settings.py yang berada pada folder utama. Lalu agar MVT dapat terjadi maka diperlukan routing fungsi `show_main` dengan menambahkan path `show_main` pada `urlspattern` di _file_ urls.py , Lalu pada _folder_ utama projek saya mengubah _file_ urls.py dengan menambahkan isi dari `urlspattern` dengan menambah _path_ ke `main.urls`. Lalu agar memungkinkan _deploy_ aplikasi pada localhost dan juga pada pws saya menambahkan url atau port yang akan digunakan sebagai sarana _hosting_ . 


Lalu untuk memfasiliatsi pengembangan yang lebih lanjut atau dalam maksud ini _backend_ maka saya membuat model pada _file_ models.py dimana berisi atribut `name`, `price` dan `description`. Lalu untuk mengintegrasikan seluruh model yang baru didefinisikan saya menggunkan perintah `python manage.py makemigrations`. Lalu setelah melakukan perubahan untuk seluruh kode yang diperlukan kita lakukan _commit_ menuju github dengan melakukan operasi `git add .`, `git commit -m "comment"`, `git push`.

---

### **Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.**
![plot](./image/bagan.png)

---

### **Jelaskan fungsi git dalam pengembangan perangkat lunak!**
Git dalam perangkat lunak berfungsi untuk melakukan penyimpanan perubahan atau tiap versi dalam pengembangan suatu aplikasi, sehingga kita masih memiliki simpanan dari berbagai perubahan yang dilakukan. Selain itu, git juga dapat membantu dalam melakukan kolaborasi dalam pengembangan suatu aplikasi dimana tiap pengembang dapat di-_track_ dan dapat dengan mudah melihat perubahan yang dilakukan oleh orang lain.

---

### **Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?**
a. Full-Stack Framework yang Terstruktur
Django adalah full-stack framework, yang berarti ia menyediakan alat untuk semua bagian dari aplikasi web, mulai dari frontend hingga backend. Ini termasuk routing, manajemen database, authentication, hingga keamanan. Pemula yang belajar Django bisa memahami cara kerja aplikasi secara menyeluruh tanpa harus menggunakan banyak alat atau framework lain.

b. Pendekatan Batteries Included
Django mengikuti filosofi batteries included, yang berarti framework ini sudah dilengkapi dengan fitur-fitur dasar yang dibutuhkan untuk membangun aplikasi web. Ini memudahkan pemula karena mereka tidak perlu mengonfigurasi terlalu banyak komponen eksternal. Contoh fiturnya meliputi ORM (Object-Relational Mapping), sistem manajemen admin, otentikasi pengguna, dan sistem templating yang kuat.

c. ORM yang Memudahkan Pengelolaan Database
Django memiliki ORM bawaan yang memungkinkan pengembang untuk bekerja dengan database tanpa harus menulis banyak kode SQL. Ini sangat membantu pemula, karena mereka dapat fokus pada logika aplikasi dan belajar manajemen database dengan cara yang lebih intuitif dan user-friendly.

d. Dokumentasi yang Lengkap dan Komunitas yang Aktif
Django dikenal memiliki dokumentasi yang sangat komprehensif dan jelas. Ini sangat penting untuk pembelajaran, karena pemula bisa mendapatkan panduan yang jelas tentang bagaimana menggunakan setiap fitur. Selain itu, komunitas Django juga sangat aktif, sehingga pemula dapat dengan mudah menemukan tutorial, forum, dan contoh kasus dari pengembang lain.

e. Fokus pada Praktik Best Practices
Django dirancang dengan prinsip-prinsip best practices dalam pengembangan perangkat lunak, seperti keamanan (CSRF protection, SQL injection protection), skema URL yang bersih, serta penggunaan arsitektur Model-View-Template (MVT). Penggunaan Django membantu pemula memahami pentingnya struktur yang baik dan kode yang teratur sejak awal pembelajaran.

f. Keamanan Bawaan yang Tinggi
Django secara otomatis mengimplementasikan banyak langkah keamanan dasar, seperti perlindungan terhadap serangan SQL Injection, Cross-Site Scripting (XSS), dan Cross-Site Request Forgery (CSRF). Ini memberi pengembang pemula keamanan dasar tanpa harus memahaminya secara mendalam dari awal.

g. Kemudahan Skalabilitas
Django adalah framework yang sering digunakan oleh startup hingga perusahaan besar, seperti Instagram dan Pinterest, karena mampu menangani aplikasi yang skalanya besar. Mempelajari Django memberikan pemahaman kepada pemula bahwa framework ini dapat digunakan untuk proyek kecil hingga besar, dan mereka tidak perlu mengganti framework ketika proyek mereka berkembang.

h. Sesuai untuk Pengembangan Cepat
Django memudahkan pengembangan prototipe dengan cepat karena berbagai alat yang sudah terintegrasi. Pengembang pemula dapat melihat hasil dari kode mereka lebih cepat, yang membantu mereka tetap termotivasi dalam proses pembelajaran.

i. Dukungan Terhadap REST API dan Teknologi Modern
Django sangat mendukung pengembangan REST API dengan Django REST Framework (DRF). Hal ini memberi kesempatan kepada pengembang pemula untuk belajar tentang bagaimana membangun API modern yang berinteraksi dengan berbagai frontend frameworks seperti React, Vue, atau Angular.

---

### **Mengapa model pada Django disebut sebagai ORM?**
Model pada Django disebut sebagai ORM (Object-Relational Mapping) karena Django menggunakan pendekatan ini untuk menghubungkan antara objek Python dengan database relasional. ORM memungkinkan pengembang untuk berinteraksi dengan database menggunakan objek-objek Python, tanpa harus menulis SQL secara langsung. Penjelasan lebih lengkap:

a. Objek (Object): Dalam Django, model didefinisikan sebagai kelas Python. Setiap kelas model merepresentasikan tabel di database, dan setiap atribut di kelas tersebut merepresentasikan kolom dalam tabel.

b. Relasional (Relational): Django ORM bekerja dengan database relasional seperti PostgreSQL, MySQL, SQLite, dll. Basis data relasional menyimpan data dalam bentuk tabel yang berhubungan satu sama lain melalui foreign key, primary key, dan relasi lainnya.

c. Mapping: ORM memetakan (mapping) objek di Python (model dan atribut) ke struktur tabel dan kolom di database. Dengan menggunakan ORM, pengembang dapat membuat, membaca, memperbarui, dan menghapus data (operasi CRUD) di database melalui kode Python, tanpa menulis query SQL.

# Tugas 3
### **Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?**
Data delivery, atau pengiriman data, adalah proses mendistribusikan informasi dari satu sistem ke sistem lain dalam sebuah platform. Dalam pengembangan suatu aplikasi data delivery sangat penting karena merupakan otak dalam komunikasi dan operasi antara komponen atau pengguna pada platform tersebut. Adapun bila dijabarkan dapat terjelaskan sebagai berikut:

1. Pertukaran Data yang Efisien
Dalam platform apa pun, data harus ditransfer antara berbagai modul, layanan, atau pengguna. Data delivery yang efisien memastikan bahwa informasi dikirimkan dengan cepat, akurat, dan pada waktu yang tepat, sehingga memungkinkan aplikasi berjalan lancar. Tanpa mekanisme data delivery yang andal, data bisa tertahan, terlambat sampai, atau hilang, yang dapat menyebabkan sistem tidak responsif atau tidak bekerja sesuai ekspektasi.

2. Konektivitas Antar-Komponen
Sebagian besar platform memiliki berbagai komponen atau modul yang perlu bekerja bersama untuk memberikan layanan. Misalnya, dalam aplikasi e-commerce, data pesanan, pembayaran, dan stok harus dikomunikasikan secara tepat di antara beberapa sistem (front-end, back-end, database, gateway pembayaran, dll.). Data delivery memungkinkan konektivitas antar-modul ini sehingga semua komponen dapat mengakses dan menggunakan informasi yang sama, menjaga sinkronisasi dan keakuratan data.

3. Pengalaman Pengguna yang Lebih Baik
Pengguna platform modern mengharapkan respon yang cepat dan layanan yang konsisten. Sistem data delivery yang efisien membantu memastikan bahwa pengguna mendapatkan informasi yang diinginkan secara real-time atau mendekati real-time. Misalnya, dalam aplikasi media sosial atau platform layanan streaming, data seperti pesan atau konten video harus dikirimkan segera setelah diminta oleh pengguna. Ini memastikan user experience yang lancar dan memuaskan.

4. Keamanan Data
Sistem pengiriman data yang baik juga memperhatikan keamanan dalam proses pengiriman informasi, terutama ketika data yang ditransfer adalah sensitif (misalnya, informasi pribadi, data pembayaran, dll.). Dengan adanya data delivery yang aman, platform dapat memastikan bahwa data yang dikirimkan antar-sistem tidak mudah diakses atau dimodifikasi oleh pihak yang tidak berwenang. Ini melibatkan enkripsi, otentikasi, dan kontrol akses yang kuat.

5. Replikasi dan Skalabilitas
Dalam platform besar yang mendukung banyak pengguna dan volume data yang tinggi, replikasi data dan skalabilitas sistem menjadi penting. Data delivery memungkinkan platform mendistribusikan data ke berbagai lokasi atau server yang terpisah secara geografis, sehingga platform dapat berfungsi secara efisien di bawah beban yang tinggi. Misalnya, dalam platform global seperti penyedia layanan cloud atau jaringan distribusi konten (CDN), data delivery memungkinkan pengguna di berbagai wilayah menerima layanan dengan latensi minimal.

6. Keandalan dan Redundansi
Data delivery juga memastikan bahwa data yang penting tidak hilang selama transmisi. Dalam platform dengan volume data yang tinggi, keandalan menjadi kunci. Pengiriman data yang baik dapat mencakup mekanisme redundansi, seperti replikasi data atau pengiriman ulang, untuk memastikan bahwa data selalu sampai ke tujuan meskipun terjadi kegagalan jaringan atau sistem.

7. Pengambilan Keputusan Berbasis Data
Platform yang mengandalkan data analytics untuk pengambilan keputusan (misalnya, platform e-commerce yang menggunakan data pengguna untuk personalisasi) membutuhkan data yang dikirim secara cepat dan akurat ke mesin pemrosesan data. Data delivery memastikan bahwa data dikumpulkan dari berbagai titik dalam platform dan dikirim ke sistem analitik dengan cepat untuk menghasilkan wawasan yang berguna.

8. Penghematan Biaya Operasional
Proses pengiriman data yang buruk atau tidak efisien dapat menyebabkan penggunaan sumber daya yang tidak optimal, seperti bandwidth atau server, yang pada akhirnya meningkatkan biaya operasional. Dengan sistem data delivery yang baik, penggunaan sumber daya bisa lebih terkontrol, mengurangi pemborosan dan meningkatkan efisiensi operasional platform.

9. Integrasi dengan Sistem Lain
Banyak platform harus berintegrasi dengan sistem pihak ketiga (misalnya, API dari platform lain, layanan pembayaran, atau penyedia logistik). Data delivery yang andal diperlukan agar platform dapat bertukar data dengan sistem eksternal ini secara mulus, misalnya, dalam sistem ERP atau CRM.

### **Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?**
Bagi saya alasan kepopuleran dari JSON dibanding XML adalah kemudahan dalam membaca data yang ada serta besar berkas yang lebih kecil dibandingkan XML. Sehingga memungkinkan proses _debugging_ yang lebih mudah dan juga proses pertukaran informasi yang lebih efisien

### **Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?**
Method form.is_valid() dalam Django berfungsi untuk memvalidasi data yang dikirimkan melalui form. Ketika Anda menggunakan form di Django, seperti dalam kasus formulir HTML untuk input data pengguna, validasi sangat penting untuk memastikan bahwa data yang diterima dari pengguna sudah sesuai dengan aturan yang telah ditentukan di dalam form tersebut. Dalam hal ini sebelum data diteruskan ke database telah dicek apakah setiap data yang dimasukkan oleh pengguna telah sesuai dengan format pada models, seperti _price_ haruslah diisi hanya oleh bilangan dan _name_ oleh kalimat dan sebagainya. Sehingga pada akhirnya didapatkan data yang kesannya bersih.

### **Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan**
**csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?**

**Mengapa Kita Membutuhkan csrf_token di Django?**
CSRF (Cross-Site Request Forgery) adalah jenis serangan di mana penyerang dapat memaksa pengguna untuk melakukan tindakan tidak diinginkan pada situs web tempat mereka sudah terautentikasi. csrf_token adalah mekanisme keamanan yang digunakan Django untuk melindungi aplikasi dari serangan CSRF.

Saat membuat form di Django, kita perlu menambahkan csrf_token untuk mencegah serangan ini. Token ini adalah nilai unik yang dibuat oleh server dan disisipkan dalam setiap form yang mengirimkan data melalui metode POST. Saat form dikirim, Django akan memeriksa apakah token yang dikirimkan dalam request sesuai dengan token yang diharapkan. Jika token tidak cocok atau tidak ada, Django akan menolak request tersebut karena dianggap tidak sah.

**Apa yang Terjadi Jika Tidak Menambahkan csrf_token?**
Jika kita tidak menambahkan csrf_token dalam form Django, aplikasi kita akan rentan terhadap serangan CSRF. Hal ini berarti penyerang bisa memanfaatkan kelemahan ini untuk:
    1. Mengirim permintaan yang tidak sah dari browser korban tanpa sepengetahuan mereka.
    2. Membuat korban tanpa sengaja melakukan tindakan berbahaya seperti mengubah data akun, melakukan transfer uang, atau mengirim data sensitif di aplikasi yang mereka login sebelumnya.
Tanpa csrf_token, aplikasi tidak dapat membedakan antara permintaan yang sah dari pengguna yang valid dan permintaan yang dibuat oleh penyerang. Sebagai contoh semisal penyerang telah mengetahui suatu endpoint yang tak terlindungi oleh csrf, maka apabila ada seorang pengguna yang telah terverfikasi oleh sistem dalam suatu web dan ia mengunjungi suatu halaman web yang telah disisipi kode "jahat", maka penyerang memungkin untuk menerima atau membuat _request_ yang membahayakan data pribadi korban.

### **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**
A. Membuat input form untuk menambahkan objek model pada app sebelumnya.
Pertama tama pada bagian model saya menambahkan _field_ `id` yang didesain untuk menjadi parameter unik yang membedakan suatu data dengan data yang lain
```
id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
```
Lalu untuk memfasilitasi masukkan dari pengguna saya membuat suatu berkas bernama forms.py yang ditujukan sebagai tempat masukkan dan berkas yang mempermudah proses validasi dari masukkan.
```
from django.forms import ModelForm
from main.models import NelayanEntry

class NelayanEntryForm(ModelForm):
    class Meta:
        model = NelayanEntry
        fields = ["name", "price", "description"]
```
Lalu pada berkas views.py saya menambahkan suatu fungsi baru yang berisi perintah ketika laman dari form diakses, dimana didalamnya juga dilakukan proses verifikasi dan juga perubahan dalam database apabila data yang dimasukkan ada dan benar.
```
def create_item_entry(request):
    form = NelayanEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')
    
    context = {'form': form }
    return render(request, "create_item_entry.html", context)
```
Lalu untuk memastikan laman form dapat diakses maka pada berkas urls.py saya tambahka proses _routing_ untuk laman form.
```
path('create-item-entry', create_item_entry, name='create_item_entry'),
``` 
Lalu pada laman folder saya membuat suatu kerangka html pada direktori templates pada main, dengan anma create_item_entry.html untuk memudahkan pengguna memasukkan data yang mereka inginkan pada aplikasi dan juga sebagai bahan keamanan tambahan, form disusun dengan menggunakan protokol _csrf_ sehingga setiap _request_ yang valid hanya bisa dilakukan apabila dilakukan pada laman atau proses yang semestinya.

B. Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.
Untuk menyelesaikan ini pada berkas views.py untuk melihat object secara umum, saya mengakases semua data yang ada pada database dengan menggunakan perintah
```
data = NelayanEntry.objects.all()
```
dan untuk data yang memerlukan id saya melakukan pencarian data pada database dengan menggunkan perintah
```
data = NelayanEntry.objects.filter(pk=id)
```
lalu untuk menampilkan dalam bentuk json kita isi pada `content_type` pada httpResponse dengan `application/json` dan untuk XML dengan `application/xml`.

C. Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin B.
Untuk melakukan ini pada berkas urls.py pada direktori main untuk setiap fungsi yang dibuat pada poin b masing saya buat _path_ dari fungsi - fungsi tersebut
```
path('xml/', show_xml, name='show_xml'),
path('json/', show_json, name='show_json'),
path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
```
dimana pada sisi paling kiri merepresentasikan _link_ pada web dan sisi tengah nama fungsi yang akan dipanggil. 

Lalu setelah step A, B dan C telah selesai kita dapat menjalankan aplikasi dengen menekan perintah `python manage.py runserver` yang mana akan menjalankan aplikasi kita pada _local_ komputer.

### **Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.**
![plot](./image/json_all.png)
![plot](./image/json_id.png)
![plot](./image/xml_all.png)
![plot](./image/xml_id.png)