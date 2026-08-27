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
    "AEK Athens": (38.03720222237312, 23.741576096319555),
    "Arsenal": (51.555108754949096, -0.108421260631924),
    "Aston Villa": (52.50914432178864, -1.884825718246934),
    "Atletico Madrid": (40.43624860348145, -3.5994819035666348),
    "Barcelona": (41.36461082529342, 2.155793990914767),
    "Bayern München": (48.21878832276317, 11.624656610336265),
    "Bodø/Glimt": (67.27665450117082, 14.384291840415571),
    "Borussia Dortmund": (51.49261549157945, 7.451846668200702),
    "Club Brugge": (51.193515443276176, 3.1805739965119835),
    "Como": (45.81387854898877, 9.072386225397391),
    "Fenerbahçe": (40.98769646736312, 29.036858109951133),
    "Feyenoord": (51.89389757679882, 4.523170039388487),
    "Galatasaray": (41.103377155785694, 28.99104339646617),
    "Inter": (45.478111358777156, 9.12390648604918),
    "LASK": (48.29366569610336, 14.276691674161619),
    "Leipzig": (51.34575206890372, 12.348269696910545),
    "Lens": (50.432898374147605, 2.814970626119379),
    "Lille": (50.61191029027531, 3.130473980097893),
    "Liverpool": (53.43088588002024, -2.9608651246402182),
    "Man City": (53.48316975662247, -2.200362874005075),
    "Man United": (53.463061196544615, -2.2913392765397913),
    "Napoli": (40.82796894440031, 14.193039638779714),
    "PSG": (48.84143737133421, 2.253039668044727),
    "Porto": (41.16177797467342, -8.583593197021917),
    "PSV": (51.44175406126967, 5.4674263227708915),
    "Real Betis": (37.35651775636523, -5.981700974875139),
    "Real Madrid": (40.453030507459914, -3.6883337035658155),
    "Roma": (41.93388355800951, 12.454684807810292),
    "Sabah": (40.39734494500955, 49.852380980029395),
    "Shakhtar Donetsk": (48.021194549545605, 37.81016423521044),
    "Slavia Praha": (50.067442771381714, 14.471488554118),
    "Slovan Bratislava": (48.16321997838616, 17.13686247910215),
    "Sporting CP": (38.76125503550037, -9.160760035352318),
    "Stuttgart": (48.792285869636906, 9.232069250517972),
    "Viking": (58.91457597884756, 5.7310145971032735),
    "Villarreal": (39.94409140909855, -0.10348142635532458) 
}

for team, (lat, lon) in teams.items():
    ax.plot(lon, lat, 'ro', markersize=2, transform=ccrs.PlateCarree(), label='')


plt.title('UEFA Champions League 2026-27', fontsize=15)
plt.savefig('ChampionsLeague/LeaguePhase/UEFA Champions League 2026-27.png', dpi=300, bbox_inches='tight')
plt.show()