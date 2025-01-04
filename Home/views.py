from django.shortcuts import render

# def home(request):
#     return render(request, 'home.html')

def home(request):
    categorii = [
        {"id": 1, "denumire": "Generatoare", "poza": "https://i.postimg.cc/tRSBZ9dR/eu30-removebg-preview.png", "linkPaginaProduse": "/productManagement/produse/generatoare"},
        {"id": 2, "denumire": "Mai Compactor", "poza": "https://ntc.cz/thumbcache/k5qaw0qw051g8wo2au9jtwmswl1eaqkh1flnhan3qqu31w2ot9s5slu-wjgmszxakwwyjtl3251fqj5i5dlagx-zltt0bjgzrflesdie.png", "linkPaginaProduse": "/productManagement/produse/mai-compactor"},
        {"id": 3, "denumire": "Placi Compactoare", "poza": "https://ntc.cz/thumbcache/k5qaw0qw051g8wo2au9jtwmswl1eaqkh1flnhan3qmqs2oexhvpjnvkpfoq3qatat1ifn79qwwzp51pi5mxvmiqjt0dfmuna0fyuiafv8.png", "linkPaginaProduse": "/productManagement/produse/placi-compactoare"},
        {"id": 4, "denumire": "Taietor Beton", "poza": "https://i.postimg.cc/GtHJJsPL/shopping-removebg-preview.png", "linkPaginaProduse": "/productManagement/produse/taietor-beton"},
        {"id": 5, "denumire": "Motoare Honda", "poza": "https://i.postimg.cc/W3f03bBQ/Motor-Honda-GX390-jpg-removebg-preview.png", "linkPaginaProduse": "/productManagement/produse/motoare-honda"},
        {"id": 6, "denumire": "Motopompe de apa", "poza": "https://i.postimg.cc/Kj6LPpvf/wh20-removebg-preview.png", "linkPaginaProduse": "/productManagement/produse/motopompe-de-apa"},
        {"id": 7, "denumire": "Ciocane Hidraulice", "poza": "https://i.postimg.cc/k4ZtCY8C/R-removebg-preview.png4", "linkPaginaProduse": "/productManagement/produse/ciocane-hidraulice"},
        {"id": 8, "denumire": "Piese Miniexcavator", "poza": "https://i.postimg.cc/c1rj0F2b/14559741-piese-motor-perkins-jcb-catbobcat-miniexcavator-1-removebg-preview.png", "linkPaginaProduse": "/productManagement/produse/piese-miniexcavator"},
        {"id": 9, "denumire": "Cilindru Compactor", "poza": "https://i.postimg.cc/CKhPt7bJ/k5qaw0qw051g8wo2au9jtwmswl1eaqkh1flnhan3orocd7gkj13oego0ec2mpifgbj6ubkfzhbhxxblga-removebg-preview.png", "linkPaginaProduse": "/productManagement/produse/cilindru-compactor"},
    ]
    return render(request, 'home.html', {"categorii": categorii})