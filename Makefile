push: # Build Hugo and push
	hugo && git add . && git commit -m "$(m)"

run:
	hugo serve