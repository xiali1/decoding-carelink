
import sys
import argparse
import textwrap

from pprint import pprint, pformat
from binascii import hexlify
# from datetime import datetime
# from scapy.all import *

from decocare import lib, history

from decocare.history import parse_record

def get_opt_parser( ):
  parser = argparse.ArgumentParser( )
  parser.add_argument('infile', nargs="+",
                      default=sys.stdin,
                      type=argparse.FileType('r'),
                      help="Find dates in this file.")

  parser.add_argument('--out',
                      default=sys.stdout,
                      type=argparse.FileType('w'),
                      help="Write records here.")
  return parser

##
# move to history.py
#


def eat_nulls(fd):
  nulls = bytearray( )
  for B in iter(lambda: bytearray(fd.read(1)), bytearray("")):
    if B[0] == 0x00:
      nulls.extend(B)
    else:
      fd.seek(fd.tell( ) - 1)
      break
  print "found %s nulls" % len(nulls)
  return nulls

def find_records(stream):
  records = [ ]
  errors  = [ ]
  bolus = bytearray( )
  extra = bytearray( )
  opcode = ''

  for B in iter(lambda: bytearray(stream.read(2)), bytearray("")):

    if B == bytearray( [ 0x00, 0x00 ] ):
      print ("#### STOPPING DOUBLE NULLS @ %s," % stream.tell( )),
      nulls = eat_nulls(stream)
      print "reading more to debug %#04x" % B[0]
      print lib.hexdump(B, indent=4)
      print lib.int_dump(B, indent=11)

      extra = bytearray(stream.read(32))
      print "##### DEBUG HEX"
      print lib.hexdump(extra, indent=4)
      print "##### DEBUG DECIMAL"
      print lib.int_dump(extra, indent=11)
      # print "XXX:???:XXX", history.parse_date(bolus).isoformat( )
      break
    record = parse_record( stream, B )
    records.append(record)

  return records

def main( ):
  parser = get_opt_parser( )
  opts = parser.parse_args( )
  tw_opts = {
    'width': 50,
    'subsequent_indent': '          ',
    'initial_indent': '       ',
  }
  wrapper = textwrap.TextWrapper(**tw_opts)
  for stream in opts.infile:
    print "## START %s" % (stream.name)
    records = find_records(stream)
    i = 0
    for record in records:

      prefix = '#### RECORD {} {}'.format(i, str(record))
      print record.pformat(prefix)
      i += 1
    print "`end %s: %s records`" % (stream.name, len(records))
    stream.close( )

if __name__ == '__main__':
  import doctest
  failures, tests = doctest.testmod( )
  if failures > 0:
    print "REFUSING TO RUN DUE TO FAILED TESTS"
    sys.exit(1)
  main( )
#####
# EOF
