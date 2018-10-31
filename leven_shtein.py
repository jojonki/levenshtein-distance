class LevenShtein:
    def __init__(self):
        pass

    @staticmethod
    def edit_distance(strA, strB, normalize=True, verbose=False):
        LA = len(strA) + 1
        LB = len(strB) + 1
        dp = [[0] * LA for i in range(LB)] # (LB, LA)

        for i in range(LA):
            dp[0][i] = i

        for j in range(LB):
            dp[j][0] = j

        for i in range(1, LA):
            for j in range(1, LB):
                cost = 0 if strA[i-1] == strB[j-1] else 1 # -1 for <BOS>
                dp[j][i] = min(
                               dp[j-1][i] + 1,     # insertion
                               dp[j][i-1] + 1,     # deletion
                               dp[j-1][i-1] + cost # substitution
                           )

        if verbose:
            print(['-'] + [c for c in strA])
            for j in range(LB):
                if j == 0:
                    print('-', dp[j])
                else:
                    print(strB[j-1], dp[j])

        ed = dp[LB-1][LA-1]

        if normalize:
            ed /= max(LA - 1, LB - 1)

        return ed
