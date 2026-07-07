run-script:
	python3 ${COMPETITION}/${ROUND}/$(SEASON).py

champions-league-2025-26:
	make run-script COMPETITION=ChampionsLeague ROUND=LeaguePhase SEASON=ChampionsLeague2025-26
champions-league-2025-26-eurasia:
	make run-script COMPETITION=ChampionsLeague ROUND=LeaguePhase SEASON=ChampionsLeague2025-26-Eurasia
champions-league-2026-27-first-round:
	make run-script COMPETITION=ChampionsLeague ROUND=1stRound SEASON=2026-27

conference-league-2025-26:
	make run-script COMPETITION=ConferenceLeague SEASON=ConferenceLeague2025-26

europa-league-2025-26:
	make run-script COMPETITION=EuropaLeague SEASON=EuropaLeague2025-26