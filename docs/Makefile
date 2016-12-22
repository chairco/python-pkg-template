# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SPHINXPROJ    = Demo
SOURCEDIR     = .
BUILDDIR      = _build
ALLSPHINXOPTS = doctrees

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile coverage

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# @echo $(shell pwd)/conf.py
# @echo sphinx-build -b coverage -d _build/doctrees   . _build/coverage
# @echo $(SPHINXBUILD) -b coverage -d $(BUILDDIR)/$(ALLSPHINXOPTS)  $(SOURCEDIR) $(BUILDDIR)/coverage
# @$(SPHINXBUILD) -b coverage $(ALLSPHINXOPTS) $(SOURCEDIR) $(BUILDDIR)/coverage
coverage:  
	$(SPHINXBUILD) -b coverage -d $(BUILDDIR)/$(ALLSPHINXOPTS)  $(SOURCEDIR) $(BUILDDIR)/coverage
	@echo
	@cat $(BUILDDIR)/coverage/python.txt
