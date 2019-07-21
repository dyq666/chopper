import argparse
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from argparse import Namespace


def get_template(type_: str) -> str:
    tmpl = 'template/%s.conf' % type_
    with open(tmpl, 'r') as f:
        return f.read()


def handle_git(args: 'Namespace') -> None:
    type_ = 'git'
    with open('conf/%s.conf' % type_, 'w') as f:
        name, email = args.name, args.email
        tmpl = get_template(type_)
        f.write(tmpl.format(name=name, email=email))


parser = argparse.ArgumentParser(description='Desc: generate some config files.')
sub_parser = parser.add_subparsers()

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
