#!/usr/bin/env python3

# import modules used here -- sys is a very standard one
import sys, argparse, logging, time

def fn(a, b):
  # function body
  return

# Gather our code in a main() function
def main(args, loglevel):
  logging.basicConfig(format="%(levelname)s: %(message)s", level=loglevel)

  # TODO Replace this with your actual code.
  logging.debug("a: %s, b: %s" % (args.aArray, args.bArray))

  start_time = time.time()
  logging.info(fn(args.aArray, args.bArray))
  logging.info("--- %s seconds ---" % (time.time() - start_time))

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
  parser = argparse.ArgumentParser(description = "Does a thing to some stuff.",
                                    epilog = "As an alternative to the commandline, params can be placed in a file, one per line, and specified on the commandline like '%(prog)s @params.conf'.",
                                    fromfile_prefix_chars = '@' )
  # TODO Specify your real parameters here.
  parser.add_argument("-a", "--aArray", nargs='+', type=int,
                      help = "pass ARG to the program",
                      metavar = "ARG")
  parser.add_argument("-b", "--bArray", nargs='+', type=int,
                      help = "pass ARG to the program",
                      metavar = "ARG")
  args = parser.parse_args()

  # Setup logging
  if args.verbose:
    loglevel = logging.DEBUG
  else:
    loglevel = logging.INFO

  main(args, loglevel)
