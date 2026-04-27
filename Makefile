MAIN = report
LATEX = pdflatex
FLAGS = -interaction=nonstopmode -halt-on-error

all: $(MAIN).pdf

$(MAIN).pdf: $(MAIN).tex
	$(LATEX) $(FLAGS) $(MAIN).tex
	$(LATEX) $(FLAGS) $(MAIN).tex

clean:
	rm -f *.aux *.log *.out *.toc *.lof *.lot

distclean: clean
	rm -f $(MAIN).pdf
