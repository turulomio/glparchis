## @brief Debug system argparse based
from logging import basicConfig, DEBUG, INFO, WARNING, ERROR, CRITICAL, info

## Sets debug sustem, needs
## @param args It's the result of a argparse     args=parser.parse_args()        
def argparse_parsing_debug_argument(args):
    logFormat = "%(asctime)s.%(msecs)03d %(levelname)s %(message)s [%(module)s:%(lineno)d]"
    dateFormat='%F %I:%M:%S'

    if args.debug=="DEBUG":#Show detailed information that can help with program diagnosis and troubleshooting. CODE MARKS
        basicConfig(level=DEBUG, format=logFormat, datefmt=dateFormat)
    elif args.debug=="INFO":#Everything is running as expected without any problem. TIME BENCHMARCKS
        basicConfig(level=INFO, format=logFormat, datefmt=dateFormat)
    elif args.debug=="WARNING":#The program continues running, but something unexpected happened, which may lead to some problem down the road. THINGS TO DO
        basicConfig(level=WARNING, format=logFormat, datefmt=dateFormat)
    elif args.debug=="ERROR":#The program fails to perform a certain function due to a bug.  SOMETHING BAD LOGIC
        basicConfig(level=ERROR, format=logFormat, datefmt=dateFormat)
    elif args.debug=="CRITICAL":#The program encounters a serious error and may stop running. ERRORS
        basicConfig(level=CRITICAL, format=logFormat, datefmt=dateFormat)

    info("Debug level set to {}".format(args.debug))

## Adds the commons parameter of the program to argparse
## @param parser It's a argparse.ArgumentParser
def argparse_add_debug_argument(parser):
    parser.add_argument('--debug', help="Debug program information", choices=["DEBUG","INFO","WARNING","ERROR","CRITICAL"], default="ERROR")

