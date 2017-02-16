#!/usr/bin/env bash
######################################################################
#	name		: Askeran|Logic Gate Automat Developer
#	version 	: Alpha1
#	license		: GNU GPL|v3
#	autor		: Narek Kostanyan|narek.mouse@gmail.com
#	director	: Ashot Harutyunyan
######################################################################

echo "	 _    _                          _       	"
echo "	| |  | |                        | |			"
echo "	| |  | |___  ____ ____ ____   _ | | ____ 	"
echo "	 \ \/ / _  |/ ___) _  |  _ \ / || |/ _  |	"
echo "	  \  ( ( | | |  ( ( | | | | ( (_| ( ( | |	"
echo "	   \/ \_||_|_|   \_||_|_| |_|\____|\_||_|	"
echo "	_________________________________________	"

######################################################################
#	Askeran is program makes by student of SAED for
# automating Standart Cell development.


#	Envarment variable and System configuration
export BASEDIR=$(dirname "$0") # Basedir is dir where located application
export PYTHONPATH="${PYTHONPATH}:${BASEDIR}/Tools" # Integrate Tools for easy working
export SPICESIMULATOR="hspice"

#	Runing main application
python ${BASEDIR}/MainApp
