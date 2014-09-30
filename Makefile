all: clean check-manifest viewdoc
check-manifest:
	check-manifest
clean:
	rm .long-description.html
viewdoc:
	viewdoc
