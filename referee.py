import click
import arrow
from time_referee import PowerPointManager


@click.command()
@click.option('--verbose', is_flag=True, help="Verbose mode")
@click.option('--start_time', help='Start date/time of the presentation')
@click.option('--start_now', is_flag=True,
              help='Use now as the start time of the presentation')
@click.option('--total_time_in_minutes', help='Total alotted time in minutes')
@click.argument('path')
def cli(start_time, total_time_in_minutes, verbose, path, start_now=False):
    p = PowerPointManager(Path=path)
    if (start_now):
        p.start_time = arrow.now()
    elif (start_time):
        p.start_time = arrow.get('2017-01-01 {0}'.format(start_time))
    else:
        p.start_time = arrow.get('2017-01-01 00:00:00')
    click.echo("Calculating time starting from {0}".format(p.start_time))
    p.apply_timings()
    p.save()

    click.echo("Total slides: {0}".format(p.total_slides))
    click.echo("Actual time: {0}".format(p.actual_time))
