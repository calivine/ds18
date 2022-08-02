import sys

from temp_sensor import Monitor


def _real_main(argv=None):
    Monitor().activate()


def main(argv=None):
    try:
        _real_main()
    except KeyboardInterrupt:
        sys.exit('\nERROR: Interrupted by user')


main()
