data_panen= {
    'lokasi1': {
        'nama_lokasi':'kebun A',
        'hasil_panen': {
            'padi':1200,
            'jagung':800,
            'kedelai':500
        }
    },
    'lokasi2': {
        'nama_lokasi':'kebun B',
        'hasil_panen': {
            'padi':1500,
            'jagung':900,
            'kedelai':450
        }
    },
    'lokasi3': {
        'nama_lokasi':'kebun C',
        'hasil_panen': {
            'padi':1100,
            'jagung':750,
            'kedelai':600
        }
    },
    'lokasi4': {
        'nama_lokasi':'kebun D',
        'hasil_panen': {
            'padi':1300,
            'jagung':850,
            'kedelai':550
        }
    },
    'lokasi5': {
        'nama_lokasi':'kebun e',
        'hasil_panen': {
            'padi':1400,
            'jagung':950,
            'kedelai':480
        }
    },
}

# tampilkan seluruh data dari data panen termasuk nama lokasi dan hasil panen masing masing
for i, j in data_panen.items():
    
    print(f"Lokasi : {i}")
    print(f"Nama Lokasi: {j['nama_lokasi']}")
    print(f"Hasil panen padi: {j['hasil_panen']['padi']}")
    print(f"Hasil panen jagung: {j['hasil_panen']['jagung']}")
    print(f"Hasil panen kedelai: {j['hasil_panen']['kedelai']}")
    print('-------------------------')
# tampilkan jumlah hasil panen jagung dari lokasi 2
panen_jagung_lokasi2=data_panen['lokasi2']['hasil_panen']['jagung']
print('--------------')
print('jumlah hasil panen jagung dari lokasi2: ',panen_jagung_lokasi2)
# tampilkan nama lokasi dari lokasi 3
nama_lokasi_lokasi3=data_panen['lokasi3']['nama_lokasi']
print('--------------')
print('nama lokasi dari lokasi3: ',nama_lokasi_lokasi3)
#Masukan jumlah hasil panen padi dan kedelai setiap lokasi kedalam variable yang berbeda
# Buat variabel terpisah untuk menyimpan jumlah hasil panen padi dan kedelai dari setiap lokasi
padi=[]
kedelai=[]
for i in data_panen:
    padi.append(data_panen[i]['hasil_panen']['padi'])
    kedelai.append(data_panen[i]['hasil_panen']['kedelai'])
print('hasil panen padi: ',padi)
print('hasil panen kedelai: ',kedelai)
print('------------------------')
# membuat percabangan 
for i,j in data_panen.items():
    if j['hasil_panen']['padi'] > 1300 or j['hasil_panen']['jagung'] > 800:
        print(f"lokasi {i} memerlukan perhatian khusus")
    else:
        print(f'lokasi {i} dalam kodisi baik')
# nrpadd
# 152023192






