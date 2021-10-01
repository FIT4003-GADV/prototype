# GADV Prototype

Python source code for SVG visualization alt-text generation.

View the corresponding UI
here: http://gadv-core-stack-gadvclientapp-8j49htzxzvlj.s3-website-ap-southeast-2.amazonaws.com/

## Installation

Ensure you have Python installed. It is recommended to create a virtual environment before proceeding;
see https://docs.python.org/3/tutorial/venv.html

```bash
# First clone the Git repository, including submodules
git clone --recurse-submodules git@github.com:FIT4003-GADV/prototype.git

# Next, install all requirements set out in `requirements.txt`
pip install -r requirements.txt
```

## Usage

Run the `example.py` which outputs alt-text for an SVG of your choosing, or uses the example SVG vis contained in
the `example_data/` directory.

```bash
# To use your own SVG text file, supply it as a flag
python example.py --path_to_svg=<path to an svg text file>

# Or, use the example provided
python example.py

# To view all CLI options, run:
python example.py --help
```

## Running the Development Server (INTERNAL USE)

A Flask server has been implemented to handle HTTP `POST` requests to generate alt-text for users. Simply spin up the
server by running, `python dev_server.py`. It will listen on port `5001` and exposes the `/generate` POST endpoint. Make
a `POST` request on this endpoint, supplying in the JSON body, a `svg` property with the value of a raw svg XML string
to be used for the generation.

Example `POST` `/generate` body:

```json
{
  "svg": "<svg>...</svg>"
}
```

## Acknowledgements

| :memo:        | [Beagle](https://homes.cs.washington.edu/~leibatt/beagle.html)       |
|---------------|:------------------------|

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)