import argparse
import json
from pathlib import Path
from timeline import compose

def main():
    parser = argparse.ArgumentParser(description='Compose a fictional client timeline offline')
    parser.add_argument('fixture')
    parser.add_argument('--audience', choices=['internal','client'], default='internal')
    args = parser.parse_args()
    try:
        data = json.loads(Path(args.fixture).read_text(encoding='utf-8'))
        print(json.dumps(compose(data['events'], args.audience), indent=2, sort_keys=True))
    except (OSError, ValueError, KeyError) as exc:
        parser.exit(1, f'Input error: {exc}\n')

if __name__ == '__main__':
    main()
