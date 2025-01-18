push:
	git add . && git commit -m "$(m)" && git push

sync:
	cd public && git add . && git commit -m "$(m)" && git push

run:
	hugo serve