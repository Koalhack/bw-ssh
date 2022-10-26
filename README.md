# ssh-askpass for Bitwarden

## Description
This is an `ssh-askpass` compatible implementation to ask for **passphrase** stored into your Bitwarden vault.

This does **not** extract private keys. Private keys are, well, private, and should be generated uniquely on each machine. But the passphrase can be stored in Bitwarden.

## Requirements
- Python 3, any version
- [rbw](https://github.com/doy/rbw). It's an implementation of Bitwarden in CLI, supporting both terminal and graphical master password dialog. It's way faster than the official implementation.

## Usage
`SSH_ASKPASS_REQUIRE=prefer SSH_ASKPASS="bw_askpass.py" ssh-add /home/user/.ssh/test_ed25519`

You can add environment variables in your shell profile.
