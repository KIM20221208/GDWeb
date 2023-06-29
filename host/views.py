import csv
import time
from enum import IntEnum, unique
from django.http import HttpResponse

from common.models import Customer, SteamUser
from host.Crawling import Util_cluster

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


# Create your views here.
def listorders(request):
    return HttpResponse("下面是系统中所有的订单信息。。。二级表接口实现")


#
def listcustomers(request):
    # 返回一个 QuerySet 对象 ，包含所有的表记录
    # 每条表记录都是是一个dict对象，
    # key 是字段名，value 是 字段值
    qs = Customer.objects.values()

    # 定义返回字符串
    retStr = str()
    for customer in qs:
        for name, value in customer.items():
            retStr += f'{name} : {value} | '

        # <br> 表示换行
        retStr += '<br>'

    return HttpResponse(retStr)


#
def listcustomerByPhoneNum(request):
    # 返回一个 QuerySet 对象 ，包含所有的表记录
    qs = Customer.objects.values()

    # 检查url中是否有参数phonenumber
    ph = request.GET.get('phoneNumber', None)

    # 如果有，添加过滤条件
    if ph:
        qs = qs.filter(phoneNumber=ph)

    # 定义返回字符串
    retStr = str()
    for customer in qs:
        for name, value in customer.items():
            retStr += f'{name} : {value} | '
        # <br> 表示换行
        retStr += '<br>'

    return HttpResponse(retStr)


def list_user_by_steam_ID(request):
    # 检查url中是否含有参数steamid
    steam_ID_from_remote = request.GET.get('steamID', None)
    ret_set = str()
    if steam_ID_from_remote:
        """
        
        
        """
        rank = "15"
        game_title = "Cyberpunk_2077"
        app_id = "1091500"
        last_two_weeks = "70"
        hours = "40"
        recent_play = "2-4-22"
        cluster = 0
        R = 0.3

        timeStart = time.time()  # 用来计算下列循环所用事件，开始
        path = "C:/Users/JCY/repositories/GDWeb/host"
        game = Util_cluster.Game(game_title, app_id, path)  # 声明Game对象
        l_data = list()  # 用来装用户数据
        user = Util_cluster.User(steam_ID_from_remote, last_two_weeks, hours, recent_play)
        d_UserAchievements = user.getAchievements(app_id, game.d_NormalizedGlobalAchievements)

        for k, v in d_UserAchievements.items():  # k是成就名，v列表中保存的依次是：score, unlockDate, unlockYear, week, status
            steamId, hours, lastTwoWeeks, lasPlayed, lastPlayedYear, nationality, level, badges, games, friends, \
                groups, screenshots, recommended, ifDisorder = user.getMember()
            l_data.append([steamId, hours, lastTwoWeeks, ifDisorder, lasPlayed, lastPlayedYear, nationality, level,
                           badges, games, friends, groups, screenshots, recommended, k, v[0], v[1], v[2], v[3], v[4]])

        tmpTimeEnd = time.time()
        user.closeProfileResp()  # 关闭上述用户的resp

        totalScore = float(0)
        for _, v in game.d_NormalizedGlobalAchievements.items():
            totalScore += v

        c_User = Util_cluster.NewUser(steamId=l_data[0][0], hours=l_data[0][1], lastTwoWeeks=l_data[0][2], ifDisorder=l_data[0][3],
                                      lastPlayed=l_data[0][4],
                                      nation=l_data[0][5], level=l_data[0][7], badges=l_data[0][8], games=l_data[0][9],
                                      friends=l_data[0][10], groups=l_data[0][11],
                                      screenshots=l_data[0][12], reviews=l_data[0][13], ATH=l_data[0][-1], totalScore=totalScore,
                                      fromRank="15")
        c_User.TypeTrans()
        l_user = list()  # 存放User类的列表

        for row in l_data:
            c_Achievements = Util_cluster.Achievement(Title=row[14], score=row[15], unlockDate=row[16], week=row[18], status=row[19])
            c_User.achievements.append(c_Achievements)
        l_user.append(c_User)

        l_user_last = Util_cluster.Selecting(Util_cluster.Cleaning(l_user))

        timeEnd = time.time()  # 用来计算下列循环所用事件，结束
        print("program completed! cost:", Util_cluster.time_parser(timeEnd - timeStart))

        record = SteamUser.objects.create(rank=rank,
                                 steam_ID=steam_ID_from_remote,
                                 last_two_weeks=l_user_last[0][EUserParam.LAST_TWO_WEEKS],
                                 ATH=l_user_last[0][EUserParam.ATH],
                                 score_sum=l_user_last[0][EUserParam.SCORE_SUM],
                                 status_U_count=l_user_last[0][EUserParam.STATUS_U_COUNT],
                                 level=l_user_last[0][EUserParam.LEVEL],
                                 badges=l_user_last[0][EUserParam.BADGES],
                                 games=l_user_last[0][EUserParam.GAMES],
                                 friends=l_user_last[0][EUserParam.FRIENDS],
                                 groups=l_user_last[0][EUserParam.GROUPS],
                                 screenshots=l_user_last[0][EUserParam.SCREENSHOTS],
                                 Reviews=l_user_last[0][EUserParam.REVIEWS],
                                 Cluster=cluster,
                                 R=R)

        ret_set = f"<div>Crawling done.</div><h2>The user {steam_ID_from_remote}'s profile params are:</h2><table border=1, cellspacing=0, width=300>"
        for index, value in enumerate(l_user_last[0]):
            ret_set += f"<tr><td>{EUserParam(index).name}:</td><td>{value}</td></tr>"

    return HttpResponse(ret_set)


def list_own_games_by_steam_ID(request):
    steam_ID_from_remote = request.GET.get('steamID', None)
    ret_set = str()
    # TODO: Fix random input: recent_play.
    recent_play = "2-4-22"
    if steam_ID_from_remote:
        c_user = Util_cluster.User(steam_ID_from_remote, None, None, recent_play)
        c_user.crawl_last_tow_hours()
        c_user.crawl_own_game()
        c_user.closeProfileResp()

        with open("C:/Users/JCY/repositories/GDWeb/host/Crawling/gameDisorderRank.csv", mode='r', encoding="utf-8", newline='') as file:
            csv_reader = csv.reader(file)
            # 0: rank, 1: Game name, 2: appID, 3: GD rank
            l_game_disorder_rank = list(csv_reader)

        ret_set = f"<div>Crawling done.</div><h2>The user {steam_ID_from_remote}'s own games are:</h2><table border=1, cellspacing=0, width=1000>" + \
                  "<thead><tr><th>Game Name</th><th>Your Total Play Time</th><th>Game-Disorder Rank</th></tr></thead><tbody>"
        for _, d_value in enumerate(c_user.l_own_games):
            GD_rank = -1
            for value in l_game_disorder_rank:
                if value[2] == d_value.get('appID'):
                    GD_rank = value[3]
            ret_set += "<tr>"
            # https://cdn.cloudflare.steamstatic.com/steam/apps/1184370/header.jpg
            ret_set += f"<td align=center><img src=\"https://cdn.cloudflare.steamstatic.com/steam/apps/{d_value.get('appID')}/header.jpg\" /><br />{d_value.get('gameName')}</td>" + \
                f"<td align=center>{d_value.get('totalPlayed')}</td>" + \
                f"<td align=center>{GD_rank}</td>"
            ret_set += "</tr>"
        ret_set += "</tbody></table>"

    return HttpResponse(ret_set)
