run-script:
	python3 ${COMPETITION}/$(SEASON).py

champions-league-2025-26:
	make run-script COMPETITION=ChampionsLeague SEASON=ChampionsLeague2025-26
champions-league-2025-26-eurasia:
	make run-script COMPETITION=ChampionsLeague SEASON=ChampionsLeague2025-26-Eurasia

conference-league-2025-26:
	make run-script COMPETITION=ConferenceLeague SEASON=ConferenceLeague2025-26

europa-league-2025-26:
	make run-script COMPETITION=EuropaLeague SEASON=EuropaLeague2025-26