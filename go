#!/bin/bash
set -eufo pipefail

here="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

ssh "$1" -t 'ssh-agent bash -l -c "ssh-add; tmux attach; bash"'
