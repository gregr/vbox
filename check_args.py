import sys

if len(sys.argv) < 6:
  print ((
    'printf "Incorrect number of arguments passed.\\n' +
    'usage: %s ' +
    '<exec-name> <req-vars> <opt-vars> <req-args> <opt-args> <nargs>\\n"' +
    '; exit 1')
    % sys.argv[0])
  sys.exit(1)
exec_name = sys.argv[1]
req_vars, opt_vars, req_args, opt_args = [filter(None, arg.split(' '))
                                          for arg in sys.argv[2:6]]
given_args = sys.argv[6:]

def bracket_square(val): return '[%s]' % val
def bracket_angled(val): return '<%s>' % val
def assignment(name): return "%s='${%s-}'" % (name, name)
req_var_str = ' '.join(map(assignment, req_vars))
opt_var_str = ' '.join(map(bracket_square, map(assignment, opt_vars)))
req_arg_str = ' '.join(map(bracket_angled, req_args))
opt_arg_str = ' '.join(map(bracket_square, map(bracket_angled, opt_args)))
usage_str = (
  'usage: %s %s %s %s %s' %
  (req_var_str, opt_var_str, exec_name, req_arg_str, opt_arg_str))
def error_handler(msg):
 return "printf \"%s\\n%s\\n\" 1>&2; exit 1" % (msg, usage_str)

def var_check(name, msg_template):
  msg = msg_template % name
  return 'if [[ -z "${%s+x}" ]]; then %s; fi' % (name, error_handler(msg))
def vars_check(names, msg_template):
  return '\n'.join(var_check(name, msg_template) for name in names)
print vars_check(req_vars, "missing required environment variable: '%s'")
print vars_check(opt_vars, "missing default value for variable: '%s'")

given_argcount = len(given_args)
req_argcount = len(req_args)
opt_argcount = len(opt_args)
max_argcount = req_argcount + opt_argcount
if given_argcount < req_argcount or given_argcount > max_argcount:
  arg_range = '%d' % req_argcount
  if max_argcount != req_argcount:
    arg_range += ' - %d' % max_argcount
  print error_handler(
    "arguments expected: %s\\narguments given: %d"
    % (arg_range, given_argcount))

bad_options = [given for given in given_args if given.startswith('-')]
if bad_options: print error_handler('unrecognized options: %s' % bad_options)
