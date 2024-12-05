from flask import Flask
import random
app = Flask(__name__)
gorev =["Teknolojik bağımlılık çalışması, modern bilimsel araştırmanın en ilgili alanlarından biridir.",
        "Teknolojik bağımlılıkla mücadele etmenin bir yolu, zevk veren ve ruh halini iyileştiren faaliyetler aramaktır.",
        "Sosyal ağların olumlu ve olumsuz yanları vardır ve bu platformları kullanırken her ikisinin de farkında olmalıyız.",
        "2019'da yapılan bir araştırmaya göre, insanların %60'ından fazlası akıllı telefonlarındaki iş mesajlarına işten ayrıldıktan sonraki 15 dakika içinde yanıt veriyor."]
yazi_tura=["yazı",
           "tura"]

@app.route("/")
def index():
    return f'<h1>Merhaba! Bu sayfada teknolojik bağımlılıklar hakkında bir kaç ilginç gerçeği öğrene bilirsiniz! </h1><h2><a href="/rastgele_gercek">Rastgele bir gerçeği görüntüle!</a></h2><h3><a href="/yazitura">Yazi tura</a></h3>'
    
@app.route("/rastgele_gercek")
def facts():
    return f'<p>{random.choice(gorev)}</p>'


@app.route("/yazitura")
def yazitura():
    return f'<p>{random.choice(yazi_tura)}</p>'

app.run(debug=True)