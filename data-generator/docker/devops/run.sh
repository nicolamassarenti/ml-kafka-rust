#!/bin/bash

########################################################################################################################
# Bash settings ########################################################################################################
########################################################################################################################
# abort on nonzero exitstatus
set -o errexit
# abort on unbound variable
set -o nounset
# don't hide errors within pipes
set -o pipefail

########################################################################################################################
# Arguments ############################################################################################################
########################################################################################################################
URL=$1
SLEEP=$2
ENDPOINT=$3
TOPIC=$4

########################################################################################################################
# Run ##################################################################################################################
########################################################################################################################
TAG="0.1.0"
IMAGE_NAME=data-generator

docker run  --name "${IMAGE_NAME}" \
            --rm \
            -e TOPIC "${TOPIC}" \
            "${IMAGE_NAME}:${TAG}" \
            from-url \
              --url "${URL}" \
              --sleep "${SLEEP}" \
              --endpoint "${ENDPOINT}"