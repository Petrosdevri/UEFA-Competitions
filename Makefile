run-script:
	python3 ${COMPETITION}/$(SEASON).py

champions-league-2025-26:
	make run-script COMPETITION=ChampionsLeague SEASON=ChampionsLeague2025-26