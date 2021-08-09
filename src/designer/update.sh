#!/bin/bash


function process {
    pyuic5 config.ui -o ../ui/config_ui.py --import-from=ui
}    

pyrcc5 micmuter.qrc -o ../ui/micmuter_rc.py


# process current directory ui's
process

