import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

fig, ax = plt.subplots(figsize=(12, 10), subplot_kw={'projection': ccrs.LambertConformal(
                                                    central_longitude=10, central_latitude=52, standard_parallels=(35, 65))
                                                    })
ax.add_feature(cfeature.BORDERS, edgecolor='#3c0604')
ax.add_feature(cfeature.LAND, facecolor='#d1dbdd')
ax.add_feature(cfeature.OCEAN, facecolor='#3c0604')
ax.set_extent([-25, 50, 28, 72])

teams = {
    "Anderlecht": (50.83418650643685, 4.298361225597423),
    "Ararat-Armenia": (40.17191442661409, 44.52562568277611),
    "AZ Alkmaar": (52.61280418559293, 4.742039594429526),
    "Benfica": (38.752707205633925, -9.184692003647205),
    "Beşiktaş": (41.0393833996746, 28.99448670871396),
    "Bournemouth": (50.73523324183117, -1.838286863064345),
    "Celje": (46.24646081032184, 15.269942610225852),
    "Celta": (42.21192801768349, -8.739750732314674),
    "Celtic": (55.849720495921545, -4.205601689201734),
    "Crystal Palace": (51.39832772927898, -0.0854413364029441),
    "Ferencváros": (47.475398871182655, 19.09525419680334),
    "GNK Dinamo": (45.8187095483452, 16.017984267875253),
    "Hapoel Beer-Sheva": (31.273351668578172, 34.779556678386434),
    "Hoffenheim": (49.2379582110794, 8.887594800048383),
    "Jagiellonia": (53.105904954077715, 23.149095325971675),
    "Juventus": (45.109582458719736, 7.641245510164031),
    "Lech Poznań": (52.39771916500646, 16.858068839419126),
    "Leverkusen": (51.038249476643955, 7.0022458514385715),
    "Levski Sofia": (42.70534095526849, 23.363237167710523),
    "Lillestrøm": (59.96275434987054, 11.063534310288732),
    "Lyon": (45.76522435552268, 4.982030196708722),
    "Marseille": (43.26985897112824, 5.395901496576003),
    "Milan": (45.478111358777156, 9.12390648604918),
    "NEC": (51.8224529597149, 5.837239119478045),
    "OFI": (35.336829023247354, 25.106165501139042),
    "Olympiacos": (37.94644259316806, 23.664384867479047),
    "Omonoia": (35.11453327883146, 33.36288444564949),
    "Real Sociedad": (43.30136082329405, -1.9735974254052229),
    "Rennes": (48.107451409305334, -1.7128585003488537),
    "Salzburg": (47.81627581734365, 12.998213511199374),
    "Sparta Praha": (50.0998418281038, 14.415921718421096),
    "Sturm Graz": (47.04639352883885, 15.454762920987893),
    "Sunderland": (54.91442672408934, -1.388173973101639),
    "Torreense": (39.094872838382116, -9.256632029953552),
    "Union SG": (50.89572307280521, 4.334078625837817),
    "Viktoria Plzeň": (49.750009230068265, 13.385227822070291)
}

for team, (lat, lon) in teams.items():
    ax.plot(lon, lat, 'ro', markersize=2, transform=ccrs.PlateCarree(), label='')

plt.title('UEFA Europa League 2026-27', fontsize=15)
plt.savefig('EuropaLeague/UEFA Europa League 2026-27.png', dpi=300, bbox_inches='tight')
plt.show()