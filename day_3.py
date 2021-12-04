import pandas
import copy

if __name__ == '__main__':
    # input
    with open('inputs/day_3.txt', 'r') as txt:
        df = pandas.DataFrame([[c for c in line.strip()] for line in txt.readlines()])

    def counting(t, majority_win=True, tie_breaker='1', trim=False):
        ret = ''
        for i in t.columns:
            if list(t[i]).count('1') > list(t[i]).count('0'):
                winner = '1' if majority_win else '0'
            elif list(t[i]).count('1') < list(t[i]).count('0'):
                winner = '0' if majority_win else '1'
            else:
                winner = tie_breaker
            ret = ret + winner
            if trim:
                t = t[t[i] == winner]
                if len(t) == 1:
                    return ''.join(t.values.tolist()[0])
        return ret

    # Part 1
    gamma_str = counting(df, majority_win=True, tie_breaker='1', trim=False)
    gamma = int(gamma_str, 2)
    epsilon_str = counting(df, majority_win=False, tie_breaker='0', trim=Fals3)
    epsilon = int(epsilon_str, 2)
    print(gamma*epsilon)  # 1458194

    # Part 2
    gamma_df = copy.deepcopy(df)
    gamma_str = counting(df, majority_win=True, tie_breaker='1', trim=True)
    gamma = int(gamma_str, 2)
    epsilon_str = counting(df, majority_win=False, tie_breaker='0', trim=True)
    epsilon = int(epsilon_str, 2)
    print(gamma * epsilon)  # 2829354
