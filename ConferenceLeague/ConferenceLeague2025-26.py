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
    "Aberdeen": (57.15928842855907, -2.088765231444451),
    "AEK Athens": (38.03720222237312, 23.741576096319555),
    "AEK Larnaca": (34.926261544560084, 33.597692767345436),
    "AZ Alkmaar": (52.61280418559293, 4.742039594429526),
    "Breiðablik": (64.10413610503072, -21.896775802978173),
    "Celje": (46.24646081032184, 15.269942610225852),
    "Crystal Palace": (51.39832772927898, -0.0854413364029441),
    "Drita": (42.66287546066295, 21.157021981199094),
    "Dynamo Kyiv": (50.43326418966111, 30.521860809053564),
    "Fiorentina": (43.78078670467991, 11.28267415886934),
    "Häcken": (57.719205903816786, 11.930687997428477),
    "Hamrun Spartans": (35.894847946638095, 14.415234296223476),
    "Jagiellonia": (53.105904954077715, 23.149095325971675),
    "KuPS Kuopio": (62.88462930674909, 27.671870668940713),
    "Lausanne-Sport": (46.54363708838068, 6.621969739078642),
    "Lech Poznań": (52.39771916500646, 16.858068839419126),
    "Legia Warszawa": (52.22046534086816, 21.040738126651544),
    "Lincoln Red Imps": (36.149262762508215, -5.350203132601763),
    "Mainz": (49.983942118135175, 8.224379386563536),
    "Noah": (40.26849904418598, 44.63526050991609),
    "Omonoia": (35.11453327883146, 33.36288444564949),
    "Raków": (50.7767358546731, 19.159211655668404),
    "Rayo Vallecano": (40.39188220078775, -3.658621672877595),
    "Rijeka": (45.347898599696954, 14.40220499860407),
    "Samsunspor": (41.22797891675911, 36.457686638799515),
    "Shakhtar Donetsk": (48.021194549545605, 37.81016423521044),
    "Shamrock Rovers": (53.28353527227477, -6.373694060526607),
    "Shelbourne": (53.360767102808445, -6.251099188316838),
    "Shkëndija": (42.005724898872565, 21.425585567674897),
    "Sigma Olomouc": (49.60014862499777, 17.248205639252262),
    "SK Rapid": (48.19803727403955, 16.266020996844297),
    "Slovan Bratislava": (48.16321997838616, 17.13686247910215),
    "Sparta Praha": (50.0998418281038, 14.415921718421096),
    "Strasbourg": (48.56004227489608, 7.755098710355716),
    "Universitatea Craiova": (44.314040147797385, 23.784295967794336),
    "Zrinjski Mostar": (43.34569818255276, 17.795370496579938)
}

for team, (lat, lon) in teams.items():
    ax.plot(lon, lat, 'ro', markersize=2, transform=ccrs.PlateCarree(), label='')

plt.title('UEFA Conference League 2025-26', fontsize=15)
plt.savefig('ConferenceLeague/UEFA Conference League 2025-26.png', dpi=300, bbox_inches='tight')
plt.show()