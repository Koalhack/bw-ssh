# SSH key passphrases for Bitwarden

## Description
This will help you having private keys with passphrase stored in your Bitwarden vault.

This does **not** store and extract private keys. Private keys are, well, private, and should be generated uniquely on each machine. But the passphrase can be stored in Bitwarden.

There are 2 binaries (in fact, the 2 are combined):
1. An `ssh-askpass` compatible implementation to ask for **passphrase** stored into your Bitwarden vault.
2. An `ssh-keygen` wrapper that will generate a passphrase, store it in the vault, and generate the key with it.

## Requirements
- Python 3, any version
- [amoffat/sh](https://github.com/amoffat/sh/)
- [rbw](https://github.com/doy/rbw). It's an implementation of Bitwarden in CLI, supporting both terminal and graphical master password dialog. It's way faster than the official implementation.

## Usage
### keygen
- `bw-keygen -t ed25519 -f /home/user/.ssh/test_ed25519`

### askpass
- `SSH_ASKPASS_REQUIRE=prefer SSH_ASKPASS="bw-askpass" ssh-add /home/user/.ssh/test_ed25519`
- `SSH_ASKPASS_REQUIRE=prefer SSH_ASKPASS="bw-askpass" ssh -i /home/user/.ssh/test_ed25519 user@hostname`

You can add environment variables in your shell profile.
