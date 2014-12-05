check_args() {
  eval -- "$(python "$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )/check_args.py" "$@")"
}
