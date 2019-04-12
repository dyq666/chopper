import argparse
from argparse import Namespace

parser = argparse.ArgumentParser(description='Desc: generate some config files.')
sub_parser = parser.add_subparsers()


# handler
def get_template(type_: str) -> str:
    tmpl = f'template/{type_}.conf'
    with open(tmpl, 'r') as f:
        return f.read()


def handle_git(args: Namespace) -> None:
    type_ = 'git'
    with open(f'conf/{type_}.conf', 'w') as f:
        name, email = args.name, args.email
        tmpl = get_template(type_)
        f.write(tmpl.format(name=name, email=email))


# git parser
git = sub_parser.add_parser('git')
git.add_argument('-n', '--name', dest='name', metavar='name',
                 help='your git username', required=True)
git.add_argument('-e', '--email', dest='email', metavar='email',
                 help='your git email', required=True)
git.set_defaults(func=handle_git)

# run parser
args = parser.parse_args()
args.func(args)
