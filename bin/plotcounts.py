"""Plot word counts."""

import argparse
import pandas as pd

def plotcounts(infile, outfile, xlim):
    """Plots the word frequency against the inverse rank."""
    df = pd.read_csv(infile, header=None,
                    names=('word', 'word_frequency'))
    df['rank'] = df['word_frequency'].rank(ascending=False,
                                           method='max')
    df['inverse_rank'] = 1 / df['rank']
    scatplot = df.plot.scatter(x='word_frequency',
                               y='rank', loglog=True,
                               figsize=[12, 6],
                               grid=True,
                               xlim=args.xlim)
    scatplot.figure.savefig(outfile)

def main(args):
    """Run the command line program."""
    outfile = f'results/{args.outfile}.png'
    plotcounts(args.infile, outfile, args.xlim)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('infile', type=argparse.FileType('r'),
                        nargs='?', default='-',
                        help='Word count csv file name')
    parser.add_argument('-o', '--outfile', type=str,
                        default='plotcounts',
                        help='Output image file name')
    parser.add_argument('--xlim', type=float, nargs=2,
                        metavar=('XMIN', 'XMAX'),
                        default=None, help='X-axis limits')
    args = parser.parse_args()
    main(args)

