#!/usr/bin/env bash
#/** 
#  * This script ...
#  * 
#  * Copyright (c) 2019 Christian Prior
#  * Licensed under the MIT License. See LICENSE file in the project root for full license information.
#  * 
#  * Usage: ...
#  * 
#  * @TODO: ...
#  * 
#  */


set -o nounset #exit on undeclared variable

__SCRIPTDIR=$(dirname "$0")
__SCRIPTNAME=$(basename "$0")
__VERBOSE=""                 #v
__SILENT="-s"                #v
__STARTCLEAN="false"         #c

__TEMP=$(mktemp /tmp/output.XXXXXXXXXX) || { echo "Failed to create temp file"; exit 1; }
trap "{ rm -f ${__TEMP}; }" EXIT

__usage() {
    cat << EOT
  Usage :  ${__SCRIPTNAME} [options]
  Examples:
    - ${__SCRIPTNAME}
    - ${__SCRIPTNAME} -a foo
    - ${__SCRIPTNAME} -b
    - ${__SCRIPTNAME} -a foo -b
  Options:
    -a  The option...
    -b  The option...
    -h  Display this message
EOT
}

while getopts ":a:bhv" opt; do
  case $opt in
    a) __OPTION1=$OPTARG                 ;;
    b) __OPTION2="true";
       __STARTCLEAN="true"
       ;;
    h) __usage; exit 0                  ;;
    v) __VERBOSE="-v"; __SILENT=""      ;;
    \?) echo "Invalid option -$OPTARG" >&2; echo -n "continuing "; sleep 1; echo -n "."; sleep 1; echo -n "."; sleep 1; echo ".";
        ;;
  esac;
done

#http://stackoverflow.com/questions/18215973/how-to-check-if-running-as-root-in-a-bash-script
#The script needs root permissions to get the full output of \`lshw\`
_SUDO=''
if (( $EUID != 0 )); then
    echo "This script needs root permissions to get the full output of \`lshw\`"
    while true; do sudo lshw -quiet > ${__TEMP}; break; done
  _SUDO='sudo'
fi; #from now on this is possible: $SUDO some_command
_SUDO='' #revert potential security hole until \`sudo\` is really needed further on


#Trying to keep this to a minimum.
#Script tested and developed on Ubuntu 18.04
checkrequirements() {
    echo -n "Checking requirements."
    i=0;
    type awk >/dev/null 2>&1 || { echo >&2 "This script requires awk but it is not installed. ";  i=$((i + 1)); }
    type lshw >/dev/null 2>&1 || { echo >&2 "This script requires lshw but it is not installed. ";  i=$((i + 1)); }
    type make >/dev/null 2>&1 || { echo >&2 "This script requires make but it is not installed. ";  i=$((i + 1)); }
    type gcc >/dev/null 2>&1 || { echo >&2 "This script requires gcc but it is not installed. ";  i=$((i + 1)); }

    echo "..done."
    if [[ $i > 0 ]]; then echo "Aborting."; echo "Please install the missing dependency."; exit 1; fi
} #end function checkrequirements


######################################################################
#/**
#  * Main part
#  *
#  */

#clear
echo -e "Something descriptive here...\n"
checkrequirements


if [ "${__OPTION2}" == "true" ]; then
    # startclean
    echo -n "cleaning..."
fi

#/**
#  * Now ...
#  *
#  */

# adapt this to reflect dependencies within the repository
if [ -f ${__SCRIPTDIR}/tec/phy/${__VENDOR}_${__MODEL}_${__PRODUCTID}.sh ]; then
    echo -n "Applying configuration for ${__VENDOR} ${__MODEL} with productID ${__PRODUCTID}."
    ${__SCRIPTDIR}/tec/phy/${__VENDOR}_${__MODEL}_${__PRODUCTID}.sh
    echo "..done."
fi


# check
exit 0