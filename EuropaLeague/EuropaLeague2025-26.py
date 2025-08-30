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
    "Aston Villa": (52.50914432178864, -1.884825718246934),
    "Basel": (47.541596613740765, 7.620054139134276),
    "Bologna": (44.49232723786205, 11.309986625476608),
    "Braga": (41.56253537122213, -8.42986900401819),
    "Brann": (60.36696879913837, 5.3574700976046685),
    "Celta": (42.21192801768349, -8.739750732314674),
    "Celtic": (55.849720495921545, -4.205601689201734),
    "Crvena Zvezda": (44.78321118615926, 20.464948254328448),
    "FCSB": (44.43729153165402, 26.152539996637334),
    "Fenerbahçe": (40.98769646736312, 29.036858109951133),
    "Ferencváros": (47.475398871182655, 19.09525419680334),
    "Feyenoord": (51.89389757679882, 4.523170039388487),
    "Freiburg": (48.02164567516248, 7.829685096834258),
    "Genk": (51.005027849900536, 5.533384022588333),
    "GNK Dinamo": (45.8187095483452, 16.017984267875253),
    "Go Ahead Eagles": (52.26039930728451, 6.172543910574317),
    "Lille": (50.61191029027531, 3.130473980097893),
    "Ludogorets": (43.53464024906989, 26.527571481244223),
    "Lyon": (45.76522435552268, 4.982030196708722),
    "Maccabi Tel-Aviv": (32.05171548711724, 34.76153179606482),
    "Malmö": (55.583651765942186, 12.987771497789314),
    "Midtjylland": (56.11688943588704, 8.951690210815393),
    "Nice": (43.70510885253582, 7.192609477389489),
    "Nott'm Forest": (52.93994683626029, -1.1328721925531924),
    "Panathinaikos": (38.03617218107934, 23.787610326731517),
    "PAOK": (40.61384421996823, 22.972258677816495),
    "Porto": (41.16177797467342, -8.583593197021917),
    "Rangers": (55.85317799538706, -4.3092793315287246),
    "Real Betis": (37.35651775636523, -5.981700974875139),
    "Roma": (41.93388355800951, 12.454684807810292),
    "Salzburg": (47.81627581734365, 12.998213511199374),
    "Sturm Graz": (47.04639352883885, 15.454762920987893),
    "Stuttgart": (48.792285869636906, 9.232069250517972),
    "Utrecht": (52.07839014699095, 5.145813668236076),
    "Viktoria Plzeň": (49.750009230068265, 13.385227822070291),
    "Young Boys": (46.96314525369974, 7.464885307903546)
}

for team, (lat, lon) in teams.items():
    ax.plot(lon, lat, 'ro', markersize=2, transform=ccrs.PlateCarree(), label='')

plt.title('UEFA Europa League 2025-26', fontsize=15)
plt.savefig('EuropaLeague/UEFA Europa League 2025-26.png', dpi=300, bbox_inches='tight')
plt.show()