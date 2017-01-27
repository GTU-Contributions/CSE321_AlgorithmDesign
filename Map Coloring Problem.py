import time

renkler = ['Kirmizi', 'Mavi', 'Yesil', 'Sari', 'Turuncu', 'Pembe']

bolgeler = ['Kirklareli', 'Edirne', 'Tekirdag',
          'Canakkale', 'Balikesir', 'Yalova',
          'Istanbul', 'Izmit', 'Adapazari',
          'Bilecik', 'Bursa']

komsular = {}
komsular['Kirklareli'] = ['Edirne', 'Tekirdag']
komsular['Edirne'] = ['Kirklareli', 'Tekirdag','Canakkale']
komsular['Tekirdag'] = ['Kirklareli', 'Edirne', 'Canakkale', 'Istanbul']
komsular['Canakkale'] = ['Edirne', 'Tekirdag', 'Balikesir']
komsular['Istanbul'] = ['Tekirdag', 'Izmit']
komsular['Izmit'] = ['Istanbul', 'Bilecik', 'Bursa', 'Yalova', 'Adapazari']
komsular['Yalova'] = ['Izmit', 'Bursa']
komsular['Bursa'] = ['Balikesir', 'Bilecik', 'Yalova', 'Izmit', 'Adapazari']
komsular['Bilecik'] = ['Adapazari', 'Izmit', 'Bursa']
komsular['Balikesir'] = ['Bursa', 'Canakkale']
komsular['Adapazari'] = ['Izmit', 'Bilecik', 'Bursa']

bolge_renkleri = {}

def promising(bolge, renk):
    for komsu in komsular.get(bolge): 
        komsu_rengi = bolge_renkleri.get(komsu)
        if komsu_rengi == renk:
            return False

    return True

# Bolgenin rengini return eder
def bolge_rengini_bul(bolge):
    for renk in renkler:
        if promising(bolge, renk):
            return renk

def main():

    for bolge in bolgeler:
        bolge_renkleri[bolge] = bolge_rengini_bul(bolge)

    print(bolge_renkleri)

    time.sleep(5) # Sleep 5 seconds
    
main()
