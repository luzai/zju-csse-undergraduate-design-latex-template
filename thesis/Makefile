main:
	# latexmk -xelatex -latexoption=' -interaction=nonstopmode -halt-on-error' main
	xelatex  -interaction=nonstopmode -halt-on-error main
	biber main
	xelatex  -interaction=nonstopmode -halt-on-error main
	xelatex  -interaction=nonstopmode -halt-on-error -syntex=1 main
simple:
	xelatex  -interaction=nonstopmode -halt-on-error -syntex=1 main
clean:
	# latexmk -bibtex -c 
	rm -f *.log *.aux *.synctex.gz *.toc *.bbl *.bcf *.blg *.out *.xml *.ptc
	git clean -dfX

watch: main.tex 
	fswatch -o $^ | xargs -n1 -I{} make
