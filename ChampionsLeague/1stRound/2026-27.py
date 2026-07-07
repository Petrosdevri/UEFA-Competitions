import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

fig, ax = plt.subplots(figsize=(12, 10), subplot_kw={'projection': ccrs.LambertConformal(
                                                    central_longitude=10, central_latitude=52, standard_parallels=(35, 65))
                                                    })
ax.add_feature(cfeature.BORDERS, edgecolor='#001839')
ax.add_feature(cfeature.LAND, facecolor='#d1dbdd')
ax.add_feature(cfeature.OCEAN, facecolor='#001839')
ax.set_extent([-25, 50, 28, 72])

teams = {
    "Ararat-Armenia": (40.268481229987096, 44.63527880867404),
    "Atert Bissen": (49.57707187144286, 6.114160468087361),
    "Borac Banja Luka": (44.77602565504599, 17.199519467818945),
    "Drita": (42.662867571171674, 21.1570434388719),
    "Egnatia": (41.07664300809069, 19.661718915520094),
    "ETO Győr": (47.6957971833814, 17.663751151437193),
    "Flora": (59.421301486328844, 24.732072176285037),
    "Floriana": (35.89659683799848, 14.415407169504572),
    "Iberia 1999": (41.70980701953466, 44.74623923473417),
    "Inter Club d'Escaldes": (42.504647041384544, 1.517563183053279),
    "Kairat Almaty": (43.238356034255844, 76.92414921498398),
    "Kauno Žalgiris": (54.897441467116494, 23.937342350195145),
    "KÍ Klaksvík": (62.22468685865458, -6.580281710056058),
    "KuPS Kuopio": (62.88459524483768, 27.671880492094264),
    "Larne": (54.85001009327349, -5.827069329949486),
    "Levski Sofia": (42.70534095526849, 23.363237167710523),
    "Lincoln Red Imps": (36.11070396362036, -5.347000234741018),
    "ML Vitebsk": (55.19853895174831, 30.229342204549205),
    "Petrocub Hîncești": (46.82526947988391, 28.586650210257808),
    "Riga": (56.96135048359549, 24.116373787590305),
    "Sabah": (40.48618299517072, 49.76630845380574),
    "Shamrock Rovers": (53.28354168656807, -6.3736833316902075),
    "Sutjeska": (42.784918247958935, 18.9537393253899),
    "The New Saints": (52.875937632147135, -3.0264109828567447),
    "Tre Fiori": (43.97131562891415, 12.477146129012665),
    "Universitatea Craiova": (44.31402479436847, 23.784306696630733),
    "Vardar": (42.00571692651055, 21.425585567674897),
    "Víkingur Reykjavík": (64.11696611379442, -21.852674333335674)
}

for team, (lat, lon) in teams.items():
    ax.plot(lon, lat, 'ro', markersize=2, transform=ccrs.PlateCarree(), label='')


plt.title('UEFA Champions League 2026-27', fontsize=15)
plt.savefig('ChampionsLeague/1stRound/UEFA Champions League 2026-27 (1st Round).png', dpi=300, bbox_inches='tight')
plt.show()