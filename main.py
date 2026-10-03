"""Ages of Cataria Desktop — A local helper for Ages of Cataria cat-town folders, era notes, and cozy photo albums."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='ages_of_cataria_desktop',
        description='A local helper for Ages of Cataria cat-town folders, era notes, and cozy photo albums.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Ages of Cataria Desktop')
    print('Keep the cat town on disk before an era change.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
