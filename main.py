import sys

from bucket_brain import Monitor


def _real_main(argv=None):
    Monitor(moisture=False).activate()


def main(argv=None):
    try:
        _real_main()
    except KeyboardInterrupt:
        sys.exit('\nERROR: Interrupted by user')


main()
