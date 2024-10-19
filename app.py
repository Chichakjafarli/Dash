from flask import Flask, render_template_string
import folium

app = Flask(__name__)

@app.route('/')
def home():
    # Create a map centered at Azerbaijan
    map_center = [40.4093, 49.8671]
    custom_map = folium.Map(location=map_center, zoom_start=7)

    # Define locations
    locations = [
    {"name": "23 Moscow street Baku", "coords": [40.4093, 49.8671]},
    {"name": "98 Mayakovsky street Sumqayit", "coords": [40.5907, 49.6725]},
    {"name": "35 Garayev street Ganja", "coords": [40.6820, 46.3601]},
    {"name": "62 Javadkhan street Shamkir", "coords": [40.5470, 46.1402]},
    {"name": "15 Mammadov street Mingachevir", "coords": [40.7853, 47.0520]},
    {"name": "Bakı ş. Yasamal r. Zərdabi küç 68, mənzil 7", "coords": [40.38405179776507, 49.808674423681744]}, #menzil 7?
    {"name": "Bakı ş. Yasamal r. Mətbuat pr 56, mənzil 40", "coords": [40.378887128317224, 49.80943235437027]}, #menzil 40?
    {"name": "Bakı ş. Yasamal r. İnşaatçılar pr 5", "coords": [40.376100844392724, 49.81914867761181]},
    {"name": "Bakı ş. Xətai r. General Şıxlınski 4, mənzil 10", "coords": [40.36964665720792, 49.96364818320583]}, #menzil 10?
    {"name": "Abşeron rayonu Mehdiabad qəs. Hüseyn Cavid küç ev 15", "coords": [40.500680286156324, 49.85146958321227]}, #ev 15?
    {"name": "Bakı şəh. Nərimanov ray. A. Heydərov ev 22, mənzil 30", "coords": [40.394338680397475, 49.87245512738744]}, #Menzil ?
    {"name": "Bakı ş. Əmircan qəs. Sabir küç Dalan 3", "coords": [40.42678535596055, 49.98710868919456]}, #not found sabir kucesi dalan
    {"name": "Bakı şəh. Xətai ray. M. Hadi küç ev 109, mənzil 106", "coords": [40.37867865874921, 49.94510389669804]}, #menzil ev?
    {"name": "Bakı şəh. Xətai ray. Gen. Şıxlınski ev 30c, mənzil 4", "coords": [40.3680191144922, 49.964526510189366]}, #ev menzil?
    {"name": "Bakı şəh. Suraxanı ray. Yeni Günəşli qəsəbəsi. V yaşayış massivi ev 12, mənzil 157", "coords": [40.3804011363338, 49.98236877897775]}, # ev menzil?
    {"name": "Bakı şəh. Sabunçu ray. Bakıxanov qəsəbəsi M. Vəkilov küç ev 3, mənzil 6", "coords": [0, 0]},
    {"name": "Səbail ray. Teymur Elçin ev 11, mənzil 3", "coords": [40.36296949495362, 49.82750029484455]},
    {"name": "Bakı şəh. Xətai ray. Zığ yolu ev 15, mənzil 7", "coords": [40.36637763232382, 49.939679594844720]}, #founded is 1v
    {"name": "Bakı şəh. Xətai ray. M.Hadi küç ev 58, mənzil 47", "coords": [40.378719523769554, 49.94507171018977]},
    {"name": "Hövsan qəsəbəsi Elçin Məmmədov bina 4a, mənzil 12", "coords": [40.36165864815544, 50.074906112041674]}, #founded is 3A
    {"name": "Baki sheheri, Xetai rayonu, Gence prospekti 60, bina 19, menzil 2", "coords": [40.36493784228341, 49.95790324087777]},
    {"name": "Baki sheheri, Yasamal rayonu, Yeni Yasamal 1, ev 10, menzil 164", "coords": [40.394987269770176, 49.79766694331974]},
    {"name": "Baki sheheri, Xetai rayonu, Babek prospekti ev 10F, menzil 5", "coords": [40.39221202802453, 49.91635877019634]},
    {"name": "Baki sheheri, Sabunchu rayonu, Shamil Kamilov kuchesi ev 21", "coords": [40.414788806840036, 49.97355444643812]},
    {"name": "Suraxanı ray. Yeni Günəşli qəs. AB yaş. Massivi ev 8, mənzil 16", "coords": [40.378491332229494, 49.977656527386706]},
    {"name": "Xətai ray. S.Mehmandarov ev 90, mənzil 83", "coords": [40.37190150052279, 49.969580740354786]},
    {"name": "Binəqədi ray. Cəfər Xəndan ev 16, mənzil 29", "coords": [40.41820594052163, 49.84203942871798]},
    {"name": "Xətai ray. Nəsrəddin Tusi ev 19, mənzil 115", "coords": [40.378761393494045, 49.959225725534104]},
    {"name": "Xətai ray. Nəsrəddin Tusi ev 23, mənzil 39", "coords": [40.378761393494045, 49.959225725534104]},
    {"name": "Xətai ray. Xudu Məmmədov ev 2, mənzil 84", "coords": [40.37105750657813, 49.9554360562224]},
    {"name": "Baki sheheri, Nerimanov rayonu, F.X.Xoyski kuchesi ev 104A", "coords": [40.40761599555238, 49.87326007657537]},
    {"name": "H.Eliyev adina Derin Ozuller Zavodu", "coords": [0, 0]},
    {"name": "Suraxanı ray. Yeni Günəşli qəs. AB yaş. Massivi ev 78, mənzil 4", "coords": [0, 0]},
    {"name": "Neft Emalı Zavodu", "coords": [0, 0]},
    {"name": "Nizami ray. Bəhruz Nuriyev, ev 41a 264 saylı bağça", "coords": [0, 0]},
    {"name": "Yasamal ray. H.Zərdabi ev 59a giriş c, mənzil 157", "coords": [0, 0]},
    {"name": "Binəqədi ray. Azadlıq ray ev 30, mənzil 13", "coords": [0, 0]},
    {"name": "Nəsimi ray. 4-cü mkr. 20 Yanvar küç ev 3, mənzil 52", "coords": [0, 0]},
    {"name": "Sahil qəs. Məktəbli küç ev 1, mənzil 9", "coords": [0, 0]},
    {"name": "Baki sheheri, Xezer rayonu, M.Rehmanzade kuchesi ev 16", "coords": [0, 0]},
    {"name": "Baki sheheri, Xetai rayonu, S.Vezirov kuchesi ev 75, M 10, menzil 1", "coords": [0, 0]},
    {"name": "Baki sheheri, E.Quliyev kuchesi ev 65, menzil 10", "coords": [0, 0]},
    {"name": "Sahil qəs. Bəxtiyar Əliyev ev 41, mənzil 56", "coords": [0, 0]},
    {"name": "Sahil qəs. Sahil yolu ev 8, mənzil 47", "coords": [0, 0]},
    {"name": "Sahil qəs. S.Əsgərov küç ev 16, mənzil 12", "coords": [0, 0]},
    {"name": "Sahil qəs. Şahlar Əsgərov 1, mənzil 150", "coords": [0, 0]},
    {"name": "Baki sheheri, Nerimanov rayonu, F.X.Xoyski kuchesi ev 108A, menzil 6", "coords": [0, 0]},
    {"name": "Baki sheheri, Nerimanov rayonu, Tebriz kuchesi ev 55A, menzil 24", "coords": [0, 0]},
    {"name": "Baki sheheri, Nizami rayonu, Naxchivanski kuchesi ev 66A, menzil 134", "coords": [0, 0]},
    {"name": "Baki sheheri, Nesimi rayonu, H.Seyidzade kuchesi ev 26A, menzil 6", "coords": [0, 0]},
    {"name": "Baki sheheri, Suraxani rayonu, Qarachuxur qesebesi, R.Alicanov kuchesi ev 12", "coords": [0, 0]},
    {"name": "Baki sheheri, Suraxani rayonu, Qarachuxur qesebesi, Zaur Sherifov kuchesi ev 26, menzil 63", "coords": [0, 0]},
    {"name": "Baki sheheri, Suraxani rayonu, Yeni Guneshli qesebesi, 'AB' y.s. ev 127, menzil 82", "coords": [0, 0]},
    {"name": "Baki sheheri, Nizami rayonu, Ozbekistan kuchesi 9, bina 4, menzil 117", "coords": [0, 0]},
    {"name": "Sumqayit sheheri, 14 cu mehelle, ev 112C, menzil 131", "coords": [0, 0]},
    {"name": "Baki sheheri, Nizami rayonu, B.Bayramov ev 3, menzil 96", "coords": [0, 0]},
    {"name": "Sahibkarlıq Evimiz, G.Garibov küç. 9, mənzil 9", "coords": [0, 0]},
    {"name": "Baki sheheri, Nizami rayonu, C.Cavadov ev 11, menzil 45", "coords": [0, 0]},
    {"name": "Baki sheheri, Nizami rayonu, Jafar Jabbarli küç ev 56, menzil 69", "coords": [0, 0]},
    {"name": "Baki sheheri, Yasamal rayonu, Zeynalabdin qiqili ev 56, mənzil 23", "coords": [0, 0]},
    {"name": "Baki sheheri, Yasamal rayonu, A. Həziyev küç. ev 23, mənzil 112", "coords": [0, 0]},
    {"name": "Baki sheheri, Nizami rayonu, S.İsmayılov küç. ev 8, mənzil 56", "coords": [0, 0]},
    {"name": "Baki sheheri, Xətai rayonu, 20 Yanvar küç. ev 17, mənzil 30", "coords": [0, 0]},
    {"name": "Baki sheheri, Xətai rayonu, 20 Yanvar küç. ev 30, mənzil 16", "coords": [0, 0]},
    {"name": "Baki sheheri, Xətai rayonu, 20 Yanvar küç. ev 20, mənzil 34", "coords": [0, 0]},
    {"name": "Baki sheheri, Xətai rayonu, 20 Yanvar küç. ev 29, mənzil 56", "coords": [0, 0]},
    {"name": "Baki sheheri, Xətai rayonu, 20 Yanvar küç. ev 40, mənzil 100", "coords": [0, 0]},
    {"name": "Baki sheheri, Xətai rayonu, 20 Yanvar küç. ev 15, mənzil 21", "coords": [0, 0]},
    {"name": "Baki sheheri, Xətai rayonu, 20 Yanvar küç. ev 8, mənzil 19", "coords": [0, 0]},
]

    # Add markers to the map
    for location in locations:
        folium.Marker(
            location["coords"],
            popup=location["name"]
        ).add_to(custom_map)

    # Generate HTML for the map
    map_html = custom_map._repr_html_()
    return render_template_string(map_html)

if __name__ == '__main__':
    app.run(debug=True)
