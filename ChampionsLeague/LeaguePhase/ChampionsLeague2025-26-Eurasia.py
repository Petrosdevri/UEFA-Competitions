import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

fig, ax = plt.subplots(figsize=(12, 10), subplot_kw={'projection': ccrs.LambertConformal(
                                                    central_longitude=60, central_latitude=45, standard_parallels=(30, 60))
                                                    })
ax.add_feature(cfeature.BORDERS, edgecolor='#001839')
ax.add_feature(cfeature.LAND, facecolor='#d1dbdd')
ax.add_feature(cfeature.OCEAN, facecolor='#001839')
ax.set_extent([20, 90, 30, 60])

teams = {
    "Ajax": (52.31437534854556, 4.941837968250409),
    "Arsenal": (51.555108754949096, -0.108421260631924),
    "Atalanta": (45.709246130815075, 9.680816210196493),
    "Athletic Club": (43.264178309438726, -2.9493945804453805),
    "Atletico Madrid": (40.43624860348145, -3.5994819035666348),
    "Barcelona": (41.36461082529342, 2.155793990914767),
    "Bayern München": (48.21878832276317, 11.624656610336265),
    "Benfica": (38.752707205633925, -9.184692003647205),
    "Bodø/Glimt": (67.27665450117082, 14.384291840415571),
    "Borussia Dortmund": (51.49261549157945, 7.451846668200702),
    "Chelsea": (51.481730753346106, -0.1909471029635315),
    "Club Brugge": (51.193515443276176, 3.1805739965119835),
    "Copenhagen": (55.702731010083205, 12.572308654432899),
    "Eintracht Frankfurt": (50.06861300880093, 8.645476461324675),
    "Galatasaray": (41.103377155785694, 28.99104339646617),
    "Juventus": (45.109582458719736, 7.641245510164031),
    "Inter": (45.478111358777156, 9.12390648604918),
    "Kairat Almaty": (43.238356034255844, 76.92414921498398),
    "Leverkusen": (51.038249476643955, 7.0022458514385715),
    "Liverpool": (53.43088588002024, -2.9608651246402182),
    "Man City": (53.48316975662247, -2.200362874005075),
    "Marseille": (43.26985897112824, 5.395901496576003),
    "Monaco": (43.7275894241301, 7.415582338927073),
    "Napoli": (40.82796894440031, 14.193039638779714),
    "Newcastle": (54.97554401525206, -1.6216391315845278),
    "Olympiacos": (37.94644259316806, 23.664384867479047),
    "Pafos": (34.69345969427493, 32.93919869617208),
    "PSG": (48.84143737133421, 2.253039668044727),
    "PSV": (51.44175406126967, 5.4674263227708915),
    "Qarabağ": (40.39734494500955, 49.852380980029395),
    "Real Madrid": (40.453030507459914, -3.6883337035658155),
    "Slavia Praha": (50.067442771381714, 14.471488554118),
    "Sporting CP": (38.76125503550037, -9.160760035352318),
    "Tottenham": (51.60426023540722, -0.06620830295614855),
    "Union SG": (50.89572307280521, 4.334078625837817),
    "Villarreal": (39.94409140909855, -0.10348142635532458) 
}

for team, (lat, lon) in teams.items():
    ax.plot(lon, lat, 'ro', markersize=2, transform=ccrs.PlateCarree(), label='')


plt.title('UEFA Champions League 2025-26 (Eurasia)', fontsize=15)
plt.savefig('ChampionsLeague/UEFA Champions League 2025-26 (Eurasia).png', dpi=300, bbox_inches='tight')
plt.show()