import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

fig, ax = plt.subplots(figsize=(12, 10), subplot_kw={'projection': ccrs.LambertConformal(
                                                    central_longitude=10, central_latitude=52, standard_parallels=(35, 65))
                                                    })
ax.add_feature(cfeature.BORDERS, edgecolor='#064627')
ax.add_feature(cfeature.LAND, facecolor='#d1dbdd')
ax.add_feature(cfeature.OCEAN, facecolor='#064627')
ax.set_extent([-25, 50, 28, 72])

teams = {
    "Aarhus": (56.132028523134, 10.196579525838171),
    "Ajax": (52.31437534854556, 4.941837968250409),
    "Atalanta": (45.709246130815075, 9.680816210196493),
    "Borac Banja Luka": (44.77602565504599, 17.199519467818945),
    "Braga": (41.56253537122213, -8.42986900401819),
    "Brann": (60.36696879913837, 5.3574700976046685),
    "Brighton": (50.86157012895464, -0.08366363191912869),
    "Copenhagen": (55.702731010083205, 12.572308654432899),
    "Crvena Zvezda": (44.78321118615926, 20.464948254328448),
    "CSKA Sofia": (42.70534095526849, 23.363237167710523),
    "Egnatia": (41.07664300809069, 19.661718915520094),
    "Freiburg": (48.02164567516248, 7.829685096834258),
    "Gent": (51.01607643878104, 3.7338271772371336),
    "Getafe": (40.325734198013436, -3.7149438614249677),
    "Hajduk": (43.519540826078575, 16.431880608885734),
    "Hearts": (55.938976605141676, -3.2324298184233307),
    "Iberia 1999": (41.70980701953466, 44.74623923473417),
    "Inter Club d'Escaldes": (42.504647041384544, 1.517563183053279),
    "Jablonec": (50.714913526630426, 15.162237223953845),
    "Kairat Almaty": (43.238356034255844, 76.92414921498398),
    "Kauno Žalgiris": (54.897441467116494, 23.937342350195145),
    "KuPS Kuopio": (62.88462930674909, 27.671870668940713),
    "Lincoln Red Imps": (36.149262762508215, -5.350203132601763),
    "Lugano": (46.02374931768324, 8.961428171963522),
    "Midtjylland": (56.11688943588704, 8.951690210815393),
    "Mjällby": (56.011957821092025, 14.71623920094659),
    "Monaco": (43.7275894241301, 7.415582338927073),
    "Nordsjælland": (55.81607478513261, 12.353068586147963),
    "Pafos": (34.69345969427493, 32.93919869617208),
    "Panathinaikos": (38.03617218107934, 23.787610326731517),
    "Riga": (56.96135048359549, 24.116373787590305),
    "Sint-Truidense": (50.81347263080265, 5.16631950651933),
    "Thun": (46.74457805485401, 7.606602271566304),
    "Trabzonspor": (40.998725804934516, 39.646271262147735),
    "Twente": (52.236540758086925, 6.837860845270245),
    "Universitatea Craiova": (44.314040147797385, 23.784295967794336)
}

for team, (lat, lon) in teams.items():
    ax.plot(lon, lat, 'ro', markersize=2, transform=ccrs.PlateCarree(), label='')

plt.title('UEFA Conference League 2026-27', fontsize=15)
plt.savefig('ConferenceLeague/UEFA Conference League 2026-27.png', dpi=300, bbox_inches='tight')
plt.show()