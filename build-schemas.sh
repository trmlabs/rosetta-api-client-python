#!/bin/bash

cd "$(dirname "${BASH_SOURCE[0]}")"

datamodel-codegen --input api.json --output pyrosetta/schemas.py --field-constraints