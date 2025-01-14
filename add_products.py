import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sellWebsite.settings')
django.setup()

from productManagement.models import Product

products = [
    {"name": "Generator de curent TR-20 D", "price": 0, "stock": 50, "image_url": "https://i.pepita.hu/images/product/17076426/generator-de-curent-tagred-ta2800gh-2800-w-230-v-stabilizator-de-tensiune_111507782_300x300.webp", "category": "Generatoare", "tehnic_file": "Generator_de_curent_tr_20_D.jpeg"},
    {"name": "Generator de curent TR-27 KV", "price": 0, "stock": 30, "image_url": "https://www.bing.com/images/search?view=detailV2&ccid=dwvHpRLI&id=A1B6B1BE98C61059FA9428A871C05BE80DC4F986&thid=OIP.dwvHpRLIM9aqDe5LJdC_PQHaD4&mediaurl=https%3a%2f%2fsmadshop.md%2fimage%2fcache%2fproduct%2finstrumenty%2fgeneratory%2ftresz%2fdizelnyj-generator-tresz-tr-27-kv-na-pricepe-1200x630.jpg&cdnurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR.770bc7a512c833d6aa0dee4b25d0bf3d%3frik%3dhvnEDehbwHGoKA%26pid%3dImgRaw%26r%3d0&exph=630&expw=1200&q=Generator+de+curent+tr-27+kv&simid=608050937814548378&FORM=IRPRST&ck=B8B1EF8CF3B00B2520E7381CF701A36A&selectedIndex=0&itb=0", "category": "Generatoare", "tehnic_file": "Generator_de_curent_tr_27_kv.png"},
    {"name": "Generator de curent TR-22 LV", "price": 0, "stock": 30, "image_url": "https://www.bing.com/aclick?ld=e8nIZl49lX_dCNRlywStFMDDVUCUyE6U86EAoCjMDWv4Hk97v9DTqHImO8i4IXvoTF3qJcr2GPzQc508BPEDjf35v-o0pMVPX4OwhhuB2GuF9R9Earhnz1wIuxo7EoRt11wjp05OqsnKVc4UB-Byheh9l8s0ZaTCoreRJmsiPYu8rAub-r&u=aHR0cHMlM2ElMmYlMmZwZXBpdGEuY29tJTJmcm8lMmZhZ3JlZ2F0b3JpLWMxOTAxJTJmZ2VuZXJhdG9yLWRlLWN1cmVudC1wZS1tb3RvcmluYS1wbS1hZ3ItNjUwMG1kLTY1LWt3LXBvd2VybWF0LXBtMTIyNC1wMTI1NzY3MjIlM2Ztc2Nsa2lkJTNkZTU0NDAwOTkzMmNlMTExNDRjOTg2NzFmNTEwMmIzM2UlMjZ1dG1fc291cmNlJTNkYmluZyUyNnV0bV9tZWRpdW0lM2RjcGMlMjZ1dG1fY2FtcGFpZ24lM2RBbGxfcHJvZHVjdHNfY3BjX3Nob3BwaW5nJTI2dXRtX3Rlcm0lM2Q0NTg3MzY4Njc4MzU4MjMyJTI2dXRtX2NvbnRlbnQlM2RBZCUyNTIwZ3JvdXAlMjUyMCUyNTIzMQ&rlid=e544009932ce11144c98671f5102b33e&ntb=1&ntb=1&ntb=1&ntb=1", "category": "Generatoare", "tehnic_file": "Generator_de_curent_tr_22_lv.png"},
    {"name": "Generator de curent TR-20 L", "price": 0, "stock": 30, "image_url": "https://www.bing.com/aclick?ld=e89GkxhGz6eJBs_ZmP6nvsZjVUCUxecvm0Uvd8PR2yu1wd48F3l4hAA7ZeekywpReRfcJrws5e6LZnb2aKXxV1kdUnBWuqk_psB2hTcJvoM8KfLJ0g_rhfAM5bLESZ8L866kfMtp7A8snj6kOBLrmkPs1jlRsteLRxvXXnJVPBBmpIiWp3&u=aHR0cHMlM2ElMmYlMmZwZXBpdGEuY29tJTJmcm8lMmZhZ3JlZ2F0b3JpLWMxOTAxJTJmZ2VuZXJhdG9yLWRlLWN1cmVudC10YWdyZWQtdGExMTcwMGdoLTExNzAwdy0yMzB2LXN0YWJpbGl6YXRvci1kZS10ZW5zaXVuZS0yNS1sLXAxNzA3NjQxNiUzZm1zY2xraWQlM2QyZGYwMTdmMTM2N2MxOTQ3ODk1OTcwNzc1MjE1NDJkZSUyNnV0bV9zb3VyY2UlM2RiaW5nJTI2dXRtX21lZGl1bSUzZGNwYyUyNnV0bV9jYW1wYWlnbiUzZEFsbF9wcm9kdWN0c19jcGNfc2hvcHBpbmclMjZ1dG1fdGVybSUzZDQ1ODczNjg2NzgzNTgyMzIlMjZ1dG1fY29udGVudCUzZEFkJTI1MjBncm91cCUyNTIwJTI1MjMx&rlid=2df017f1367c194789597077521542de&ntb=1", "category": "Generatoare", "tehnic_file": "Generator_de_curent_tr_20_l.png"},
    {"name": "Generator de curent TR-16 AVR", "price": 0, "stock": 2, "image_url": "", "category": "Generatoare", "tehnic_file": "Generator_de_curent_trifazic_tr_16_avr.png"},
    {"name": "Generator de curent monofazic TR-7E", "price": 0, "stock": 5, "image_url": "https://www.bing.com/th?id=OIP.BH4amiDEgrgAvA2oLL-VUQHaEH&w=184&h=185&c=8&rs=1&qlt=90&o=6&dpr=1.3&pid=3.1&rm=2", "category": "Generatoare", "tehnic_file": "Generator_de_curent_monofazic_tr_7e.png"},
    {"name": "Generator de curent trifazic TR-6,5", "price": 0, "stock": 10, "image_url": "https://www.bing.com/ck/a?!&&p=264aa2a9b1f9828f2f7f85e765566102a877c9b362509068f51f148d765bd64fJmltdHM9MTczNjgxMjgwMA&ptn=3&ver=2&hsh=4&fclid=13da740c-e7bb-6ecc-3179-608be6416f69&u=a1L2ltYWdlcy9zZWFyY2g_cT1nZW5lcmF0b3IrZGUrY3VyZW50K3RyaWZhemljK3RyLTYlMmM1JmlkPTI1NzY2OUI4M0YxNzZFNkVDQjNCQjA2MzA1OUNCNzk1MjQ4Mjg1RUEmRk9STT1JUUZSQkE&ntb=1", "category": "Generatoare", "tehnic_file": "Generator_de_curent_trifazic_TR_6_5.png"},
    {"name": "Generator de curent monofazic TR-5E AVR", "price": 0, "stock": 30, "image_url": "https://www.bing.com/th?id=OIP.syGg1w7bqzlf7lH4jTJpaAHaHa&w=174&h=185&c=8&rs=1&qlt=90&o=6&dpr=1.3&pid=3.1&rm=2", "category": "Generatoare", "tehnic_file": "Generator_de_curent_monofazic_tr_5e_avr.png"},
    {"name": "Generator de curent monofazic TR-2,5", "price": 0, "stock": 60, "image_url": "https://www.bing.com/ck/a?!&&p=d7a29ad71c08e52a4a048d06367f643aa0edae778745edf511f1bef4fd134bc9JmltdHM9MTczNjgxMjgwMA&ptn=3&ver=2&hsh=4&fclid=13da740c-e7bb-6ecc-3179-608be6416f69&u=a1L2ltYWdlcy9zZWFyY2g_cT1nZW5lcmF0b3IrZGUrY3VyZW50K21vbm9mYXppYyt0ci0yJTJjNSZpZD02MTc0Qjc1OUU0RDQ0MkQxN0FCREZGRkUyNzgyNURFNUQ2NTk5MDQxJkZPUk09SVFGUkJB&ntb=1", "category": "Generatoare","tehnic_file":"Generator_de_curent_monofazic_tr_2_5.png"},
]

for product_data in products:
    product, created = Product.objects.get_or_create(**product_data)
    if created:
        print(f"Produsul {product.name} a fost adăugat.")
    else:
        print(f"Produsul {product.name} există deja.")