import asyncio
import click
import pandas as pd
from arb_hun.pipeline import run_pipeline
from arb_hun.utils import export_csv

@click.command()
@click.argument('keyword')
@click.option('--min-roi', type=float, default=None, help='Minimum ROI threshold')
@click.option('--alert/--no-alert', default=False, help='Send alerts via configured channels')
@click.option('--auto-purchase/--no-auto-purchase', default=False, help='Enable auto-purchase')
@click.option('--output-file', type=click.Path(), default='results.csv', help='Path to save results')
@click.option('--output-format', type=click.Choice(['csv','json']), default='csv', help='Output file format')
def main(keyword, min_roi, alert, auto_purchase, output_file, output_format):
    """Run pipeline and export results."""
    results = asyncio.run(run_pipeline(keyword, min_roi, alert, auto_purchase))
    df = pd.DataFrame(results)
    click.echo(df.to_string(index=False))
    if output_format == 'csv':
        export_csv(results, path=output_file)
    else:
        df.to_json(output_file, orient='records', indent=2)
    click.echo(f"Results written to {output_file}")

if __name__ == '__main__':
    main()
