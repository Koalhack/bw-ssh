#!/usr/bin/env python3

from sh import rbw, ssh_keygen, ErrorReturnCode
from pathlib import Path
import os, re, sys

KEY_PATTERN = re.compile(r" for(?: key) '?(.+?)'?: ")
RBW_ARGS = ["--folder", "ssh"]


def check_key(private_key: Path, passphrase: str):
    try:
        ssh_keygen(
            "-y", "-f", private_key, "-P", passphrase, _tty_out=False, _no_out=True
        )
        return True
    except ErrorReturnCode as ex:
        msg = ex.stderr.decode()
        print(f"Passphrase check failed: {msg}", file=sys.stderr)
        return False


if __name__ == "__main__":
    key = Path(KEY_PATTERN.search(sys.argv[1]).group(1))

    passphrase_cmd = rbw("get", *RBW_ARGS, key.name, _ok_code=[0, 1])
    # Remove new line character
    passphrase = str(passphrase_cmd)[:-1]
    # We need to check the passphrase ourself,
    # otherwise, ssh-add will call us indefinitely.
    if not check_key(key, passphrase):
        sys.exit(1)
    print(passphrase)
