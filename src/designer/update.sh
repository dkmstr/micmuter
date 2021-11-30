#!/bin/bash

PACKAGE=muter
PYSIDE=pyside6

function update_ui() {
    echo "Updating UI files..."
    for file in *.ui; do
        name=$(basename $file .ui)
	${PYSIDE}-uic -o ../${PACKAGE}/ui/${name}_ui.py ${file} --from-imports
    done
}

function compile_qrc() {
    echo "Compiling resources..."
    for file in *.qrc; do
        name=$(basename $file .qrc)
	${PYSIDE}-rcc -o ../${PACKAGE}/ui/${name}_rc.py ${file}
    done
}

# Compile qrc
compile_qrc

# And generate qt elements
update_ui
