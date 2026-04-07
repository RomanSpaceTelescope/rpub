update:
	git pull
	rpub-update

push:
	rpub-export > data/rpub-export.csv
	git add data/rpub.db data/rpub-export.csv
	git commit -m "Regular db update"
	git push

refresh:
	# Update the metadata by re-fetching all entries from the ADS API
	# this will e.g. update the citation counts and bibcodes
	rpub-export > data/rpub-export.csv
	rm data/rpub.db
	rpub-import data/rpub-export.csv

