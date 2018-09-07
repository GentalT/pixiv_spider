"""Usage:
    pixiv.py [-U <uname>] [-P <pwd>] [-T <type>] [-C <count>] [-I <interval>]
    pixiv.py [-U <uname>] [-P <pwd>] [-T <type>] [-A <artId>] [-C <count>] [-I <interval>]
    pixiv.py [-U <uname>] [-P <pwd>] [-T <type>] [-D <date>] [-C <count>] [-I <interval>]
    
Options:
    -U <uname>  Login username
    -P <pwd>    Login pwd
    -T <type>   download type,'t' total attention artists' works
                    'a' download ordering artist's works
                    'd' download target date ranking works
    -A <artId>  when type=t target artist's 
    -D <date>   when type=d target 
    -C <count>  downloads works' count [default: 20]
    -I <interval>   interval of download works,default is 0~10s [default: 10]
"""
from docopt import docopt


class Pixiv(object):
    def __init__(self, *args):
        args = dict(args[0])
        for i in args:
            if args[i]:
                self.__setattr__(i[1:], args[i])
        for i in self.__dir__():
            print(i, self.__getattribute__(i))


def main(args):
    pixiv = Pixiv(args)


if __name__ == '__main__':
    args = docopt(__doc__)
    if args.get('-T') not in ['a', 't', 'd']:
        print('params -T error, exit')
        exit(2)
    if args.get('-T') == 'a':
        if not args.get('-A'):
            print('missing params -A, use -h to see Usage')
            exit(2)
    elif args.get('-T') == 'd':
        if not args.get('-D'):
            print('missing params -D, use -h to see Usage')
            exit(2)

    main(dict(args))
