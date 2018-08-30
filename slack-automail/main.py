import click
from src.Mailer import Mailer

def abort_if_false(ctx, param, value):
    if not value:
        ctx.abort()

@click.command()
@click.option('--send_mail', default=False, help='Send email to recipients where recipients are derived from recipients.json')
def main(send_mail):
    # lets hope we dont spam everyone accidentally! ha!
    if send_mail:
        print('hh')
        mailer = Mailer()
        mailer.mail()




if __name__ == '__main__':
    main()