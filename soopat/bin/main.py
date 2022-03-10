import click

from soopat.core import Soopat


@click.group()
@click.pass_context
def cli(ctx, **kwargs):
    sp = Soopat()
    ctx.ensure_object(dict)
    ctx.obj['sp'] = sp


@click.command()
@click.pass_context
@click.option('-a', '--auto', help='register automaticly', is_flag=True)
def register(ctx, **kwargs):
    """register an account"""
    sp = ctx.obj['sp']
    sp.register(auto=kwargs['auto'])


download_epilog = '''
\b
Examples:
    soopat download -i 202010463344
    soopat download -i http://www.soopat.com/Patent/202111607937
    soopat download -i 202010463344 -u your_username -p your_password -o out.pdf
'''

@click.command(no_args_is_help=True, epilog=download_epilog)
@click.pass_context
@click.option('-i', '--url', help='the url or ID to download', required=True)
@click.option('-u', '--username', help='the username to login', prompt='username')
@click.option('-p', '--password', help='the password to login', prompt='password')
@click.option('-o', '--outfile', help='the output filename')
def download(ctx, **kwargs):
    """download the pdf for given url or ID"""
    print(kwargs)
    sp = ctx.obj['sp']
    if sp.login(kwargs['username'], kwargs['password']):
        sp.download(kwargs['url'], outfile=kwargs['outfile'])


def main():
    cli.add_command(register)
    cli.add_command(download)
    cli()


if __name__ == "__main__":
    main()