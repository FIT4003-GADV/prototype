"""
Running the "BaseWorkflow" on the SVGs in this directory.
"""
from absl import app

from base_workflow import BaseWorkflow


def main(argv):
    del argv  # Unused.

    with open('./example_data/svg.txt', 'r') as svg_file:
        svg_string = svg_file.read()

        bw = BaseWorkflow(svg_string)

        alt_text = bw.execute()
        print(alt_text)


if __name__ == '__main__':
    app.run(main)
