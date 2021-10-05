"""
Running the "BaseWorkflow" on the SVGs in this directory or a CLI-supplied SVG.
"""
from absl import app
from absl import logging
from absl import flags
import os

from base_workflow import BaseWorkflow

FLAGS = flags.FLAGS

flags.DEFINE_string('path_to_svg', './example_data/svg.txt',
                    'Path to a text-based SVG file.')


def main(argv):
    del argv  # Unused.

    logging.info('-----Running example-----')

    with open(FLAGS.path_to_svg, 'r') as svg_file:
        svg_string = svg_file.read()

        bw = BaseWorkflow(svg_string)

        alt_text = bw.execute()
        print(alt_text)


def readSVGFolder():
    charts_dir = os.getcwd() + "/example_data/svgs"
    folders = os.listdir(charts_dir)

    with open(charts_dir + "/info.txt", "w") as w:
        for i in range(len(folders)):
            logging.info(f'-----Running example {i+1}-----')
            logging.info(folders[i])
            f = open(f'{charts_dir}\{folders[i]}', 'r')
            svg_string = f.read()
            try:
                bw = BaseWorkflow(svg_string)
                alt_text = bw.execute()
                w.write(f'Example {i+1}: {alt_text}\n')
            except Exception as e:
                w.write(f'Example {i+1}: Chart type is unsupported\n')


if __name__ == '__main__':
    # app.run(main)
    readSVGFolder()
