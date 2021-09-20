"""
Main CLI interface for the prototype.
"""
from absl import app
from absl import logging
from absl import flags

FLAGS = flags.FLAGS

flags.DEFINE_bool('debug', True, 'Whether to run in debug mode.')


# flags.mark_flags_as_required(['debug'])


def main(argv):
    del argv  # Unused.
    logging.info('Hi')


if __name__ == '__main__':
    app.run(main)
