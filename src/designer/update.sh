#!/bin/bash

PACKAGE=muter

function update_ui() {
    echo "Updating UI files..."
    for file in *.ui; do
        name=$(basename $file .ui)
        pyuic5 -o ../${PACKAGE}/ui/${name}_ui.py ${file} --import-from=${PACKAGE}.ui
    done
}

function compile_qrc() {
    echo "Compiling resources..."
    for file in *.qrc; do
        name=$(basename $file .qrc)
        pyrcc5 -o ../${PACKAGE}/ui/${name}_rc.py ${file}
    done
}

# Compile qrc
compile_qrc

# And generate qt elements
update_ui