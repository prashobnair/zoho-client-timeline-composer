# zoho-client-timeline-composer (moved)

This project moved to [zoho-implementation-toolkit](https://github.com/prashobnair/zoho-implementation-toolkit) as the `timeline` module. Its full commit history was preserved there.

It composes a client-ready timeline from calls, emails, deals, and milestones — with a separate internal view for the delivery team.

## Use it now

```sh
pip install https://github.com/prashobnair/zoho-implementation-toolkit/releases/download/v0.1.0/zohokit-0.1.0-py3-none-any.whl
```

or

```sh
uv tool install git+https://github.com/prashobnair/zoho-implementation-toolkit@v0.1.0
```

The old `python cli.py events.json [--audience client]` is now:

```sh
zohokit timeline compose events.json [--audience client]
```

The client view filters internal records before producing shareable details. Reports render with `--format json|table|markdown|html` and `--out`.

## Links

- Module guide: https://prashobnair.github.io/zoho-implementation-toolkit/modules/timeline/
- What changed versus this repo: https://prashobnair.github.io/zoho-implementation-toolkit/legacy-parity/
- Source: https://github.com/prashobnair/zoho-implementation-toolkit/tree/main/src/zohokit/modules/timeline

This repository is archived and read-only.
