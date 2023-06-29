from enum import IntEnum, unique


"""
列挙型の定義。
"""


# アルファベットの月をIntに変換する。
@unique
class EMonthToInt(IntEnum):
    JAN = 1
    FEB = 2
    MAR = 3
    APR = 4
    MAY = 5
    JUN = 6
    JUL = 7
    AUG = 8
    SEP = 9
    OCT = 10
    NOV = 11
    DEC = 12


# listでの各列が表するパラメータ
@unique
class EUserParam(IntEnum):
    LAST_TWO_WEEKS = 0
    ATH = 1
    SCORE_SUM = 2
    STATUS_U_COUNT = 3
    LEVEL = 4
    BADGES = 5
    GAMES = 6
    FRIENDS = 7
    GROUPS = 8
    SCREENSHOTS = 9
    REVIEWS = 10
