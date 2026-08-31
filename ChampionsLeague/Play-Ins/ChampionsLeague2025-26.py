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
    "Atalanta": (45.709246130815075, 9.680816210196493),
    "Atletico Madrid": (40.43624860348145, -3.5994819035666348),
    "Benfica": (38.752707205633925, -9.184692003647205),
    "Bodø/Glimt": (67.27665450117082, 14.384291840415571),
    "Borussia Dortmund": (51.49261549157945, 7.451846668200702),
    "Club Brugge": (51.193515443276176, 3.1805739965119835),
    "Galatasaray": (41.103377155785694, 28.99104339646617),
    "Juventus": (45.109582458719736, 7.641245510164031),
    "Inter": (45.478111358777156, 9.12390648604918),
    "Leverkusen": (51.038249476643955, 7.0022458514385715),
    "Monaco": (43.7275894241301, 7.415582338927073),
    "Newcastle": (54.97554401525206, -1.6216391315845278),
    "Olympiacos": (37.94644259316806, 23.664384867479047),
    "PSG": (48.84143737133421, 2.253039668044727),
    "Qarabağ": (40.39734494500955, 49.852380980029395),
    "Real Madrid": (40.453030507459914, -3.6883337035658155)
}

for team, (lat, lon) in teams.items():
    ax.plot(lon, lat, 'ro', markersize=2, transform=ccrs.PlateCarree(), label='')


plt.title('UEFA Champions League 2025-26', fontsize=15)
plt.savefig('ChampionsLeague/Play-Ins/UEFA Champions League 2025-26.png', dpi=300, bbox_inches='tight')
plt.show()