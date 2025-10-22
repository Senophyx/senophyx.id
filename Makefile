push: # Build Hugo and push
	hugo && git add . && git commit -m "$(m)" && git push origin main

run:
	hugo serve