"""
Running the "BaseWorkflow" on the SVGs in this directory or a CLI-supplied SVG.
"""
from absl import app
from absl import logging
from absl import flags


from base_workflow import BaseWorkflow

FLAGS = flags.FLAGS

flags.DEFINE_string('path_to_svg', './example_data/svg.txt',
                    'Path to a text-based SVG file.')


def main(argv):
    print(argv)
    del argv  # Unused.

    logging.info('-----Running example-----')

    with open(FLAGS.path_to_svg, 'r') as svg_file:
        svg_string = svg_file.read()

        bw = BaseWorkflow(svg_string)

        alt_text = bw.execute()
        print(alt_text)


if __name__ == '__main__':
    app.run(main)
