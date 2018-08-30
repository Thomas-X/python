import click
from src.Mailer import Mailer

@click.command()
@click.option('--send_mail', default=False, help='Send email to recipients where recipients are derived from recipients.json')
def main(send_mail):
    # lets hope we dont spam everyone accidentally! ha!
    if send_mail:
        mailer = Mailer()
        mailer.mail()

if __name__ == '__main__':
    main()