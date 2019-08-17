import argparse
from functools import partial
from typing import NoReturn, TYPE_CHECKING
if TYPE_CHECKING:
    from argparse import Namespace

CONF_FORMAT = 'conf/{type}.conf'
TMPL_FORMAT = 'template/{type}.tmpl'


class CmdType:

    FlaskEnv = 'flaskenv'
    Git = 'git'

    Vars = {
        FlaskEnv: {'app', 'port'},
        Git: {'email', 'name'},
    }


def handle(args: 'Namespace', type_: str) -> NoReturn:
    conf_path = CONF_FORMAT.format(type=type_)
    tmpl_path = TMPL_FORMAT.format(type=type_)
    vars_ = CmdType.Vars[type_]

    with open(tmpl_path) as f:
        tmpl = f.read()
    with open(conf_path, 'w') as f:
        conf = tmpl.format(**{var: getattr(args, var) for var in vars_})
        f.write(conf)


parser = argparse.ArgumentParser(description='Desc: generate some config files.')
sub_parser = parser.add_subparsers()

# git parser
git = sub_parser.add_parser('git')
git.add_argument('-n', '--name', dest='name', metavar='name',
                 help='your git username', required=True)
git.add_argument('-e', '--email', dest='email', metavar='email',
                 help='your git email', required=True)
git.set_defaults(func=partial(handle, type_=CmdType.Git))

# flaskenv parser
flaskenv = sub_parser.add_parser('flaskenv')
flaskenv.add_argument('-a', '--app', dest='app', metavar='app',
                      help='your flask app path', required=False, default='app')
flaskenv.add_argument('-p', '--port', dest='port', metavar='port',
                      help='your flask run port', required=False, default=8888)
flaskenv.set_defaults(func=partial(handle, type_=CmdType.FlaskEnv))

# run parser
args = parser.parse_args()
args.func(args)
