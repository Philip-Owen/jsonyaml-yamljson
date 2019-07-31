# JSON to YAML - YAML to JSON

Converts .json files to .yaml files and vice versa.

## Initial Steps

Clone this repo and install PyYaml:

`git clone https://github.com/Philip-Owen/jsonyaml-yamljson.git`

`pip install pyyaml`

## Usage

Run `python jsonyaml.py` along with one of the following arguments:

`--json` - use this to convert .json files to .yaml files

`--yaml` - use this to convert .yaml files to .json files

ex. `python jsonyaml.py --json`

The converted files by default are created in the output folder in this directory. A prompt will allow you to set a different output path if you would like.

The script looks in the `./json` and `./yaml` folders for the files to convert but like with the output files, you can specify a different location via the prompt.

## Notes

The script will work with both YAML extensions, `.yml` and `.yaml`, when converting to JSON but only `.yaml` files will be created when converting from JSON.
