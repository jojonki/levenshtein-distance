import argparse

from leven_shtein import LevenShtein as LS


parser = argparse.ArgumentParser()
parser.add_argument('--verbose', type=int, default=0, help='print log')
parser.add_argument('--normalize', type=int, default=1, help='normalize levenshtein distance')
parser.add_argument('--mode', type=str, default='char', help='tokenization mode. char or word. word mode is only for Japanese')
parser.add_argument('--strA', type=str, help='string A')
parser.add_argument('--strB', type=str, help='string B')
args = parser.parse_args()

if args.mode == 'word':
    from janome.tokenizer import Tokenizer


def main():
    strA = '今日は良い天気だよね'
    strB = '今日は曇ってるよね'

    if args.strA:
        strA = args.strA
    if args.strB:
        strB = args.strB

    if args.mode == 'word':
        t = Tokenizer()
        strA = [token.surface for token in t.tokenize(strA)]
        strB = [token.surface for token in t.tokenize(strB)]

    v = True if args.verbose == 1 else False
    n = True if args.normalize == 1 else False
    ed = LS.edit_distance(strA, strB, normalize=n, verbose=v)
    print('Edit distance:', ed)


if __name__ == '__main__':
    main()
