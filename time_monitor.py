# coding=utf-8
import time
import subprocess
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--repeat', '-r', required=True, type=int)
parser.add_argument('--output', '-o', required=True)
parser.add_argument('cmd', nargs='*')


def monitoring_once(cmd):
    start = time.time()
    subprocess.call(cmd)
    end = time.time()
    return end - start


def monitoring(cmd, n, outfile_name):
    elapsed_all = []
    print "Going to run '" + " ".join(cmd) + "' for %d times" % n
    for i in xrange(n):
        elapsed = monitoring_once(cmd)
        elapsed_all.append(elapsed)
    with open(outfile_name, 'w') as out:
        for e in elapsed_all:
            out.write("%f\n" % e)
    avg = sum(elapsed_all) * 1.0 / len(elapsed_all)
    print "Done\nAverage runtime: %f" % avg
    print "time elapsed for each run saved at %s" % outfile_name


def main(args):
    monitoring(args.cmd, args.repeat, args.output)


if __name__ == '__main__':
    args = parser.parse_args()
    main(args)
