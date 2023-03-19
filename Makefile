.PHONY : all results test-saveconfig clean help settings

include config.mk

PARAMS=bin/plotparams.yml
DATA=$(wildcard data/*.txt)
RESULTS=$(patsubst data/%.txt,results/%.csv,$(DATA))

## all : regenerate all results.
all : results/collated.png

## results/collated.png : plot the collated results.
results/collated.png : results/collated.csv $(PARAMS) $(PLOT)
	python $(PLOT) $< --plotparams $(word 2,$^) --outfile $@

## test-saveconfig : saves plot configuration.
test-saveconfig : results/collated.csv $(PLOT)
	python $(PLOT) $< --saveconfig /tmp/test-saveconfig.yml \
	    --plotparams $(PARAMS)

## results/collated.csv : collate all results.
results/collated.csv : $(RESULTS) $(COLLATE)
	mkdir -p results
	python $(COLLATE) $(RESULTS) > $@

## results : regenerate result for all books.
results: $(RESULTS)

## results/%.csv : regenerate result for any book
results/%.csv : data/%.txt $(COUNT)
	@bash $(SUMMARY) $< "Title" 
	@bash $(SUMMARY) $< "Author" 
	python $(COUNT) $< > $@

## clean : remove all generated files.
clean : 
	rm -rvf $(RESULTS) results/collated.csv results/collated.png

## settings : show variables' values.
settings : 
	@echo COUNT: $(COUNT)
	@echo DATA: $(DATA)
	@echo RESULTS: $(RESULTS)
	@echo COLLATE: $(COLLATE)
	@echo PARAMS: $(PARAMS)
	@echo PLOT: $(PLOT)
	@echo SUMMARY: $(SUMMARY)
	@echo MAKEFILE_LIST: ${MAKEFILE_LIST}
	
## help : show this message.
help :
	@grep -h -E '^##' ${MAKEFILE_LIST} | sed -e 's/## //g' | column -t -s ':'
