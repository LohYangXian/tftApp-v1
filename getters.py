from riotwatcher import TftWatcher, ApiError
from ApiKey import *
import time


"""                     

To get player information           

"""
#Returns the String of Player's puuid 
def get_puuid(Summoner_Name,my_region):
    return tft_watcher.summoner.by_name(my_region,Summoner_Name)["puuid"]

#Returns String of Player's Summoner ID
def get_SummonerId(Summoner_Name,my_region):
    return tft_watcher.summoner.by_name(my_region,Summoner_Name)["id"]

#Returns Dictionary of Player's Rank information
def get_Rank(id,my_region):
    return tft_watcher.league.by_summoner(my_region,id)

#Returns a List of Match Codes of Player's Match History
def get_MatchHistory(puuid,my_region,count):
    return tft_watcher.match.by_puuid(my_region,puuid,count)

#Returns a Dictionary of Information regarding the Match
def get_MatchInfo(Match_Id,my_region):
    return tft_watcher.match.by_id(my_region,Match_Id)



#Returns Personal Match Info for that Match Code
def get_PersonalMatchInfo(puuid,Match_Id, my_region):
    Match_Info = get_MatchInfo(Match_Id,my_region)["info"]
    for participant in Match_Info["participants"]:
        if participant["puuid"] == puuid:
            return participant

"""

To get Champion stats

"""

#Returns a Custom List of Dictionaries of Matches (<= 4th Place? = Win , 
#Dictionary of Champions played , Dictionary of Traits played , Dictionary of Augments chosen) 
def diagnoseGames(puuid,my_region,Match_History):
    results = []
    for match in Match_History:
        personal_Match_Info = get_PersonalMatchInfo(puuid,match,my_region)
        row = []
        if personal_Match_Info["placement"] <= 4:
            row.append(True)
        else:
            row.append(False)
        row.append(personal_Match_Info["augments"])
        row.append(personal_Match_Info["traits"])
        row.append(personal_Match_Info["units"])
        results += [row]
        time.sleep(1)
    return results 

#Returns a dictionary of Champions with number of wins and losses for each champ respectively
def diagnoseChampions(results):
    champions = {}
    for row in results:
        for champion in row[3]:
            if row[0] == True:
                if champion["character_id"] not in champions:
                    champions[champion["character_id"]] = {"wins":1,"losses":0}
                else:
                    champions[champion["character_id"]]["wins"] += 1
            else:
                if champion["character_id"] not in champions:
                    champions[champion["character_id"]] = {"wins":0,"losses":1}
                else:
                    champions[champion["character_id"]]["losses"] += 1
    return champions

#Returns a list of the top 3 most played champions
def getFavouriteChamps(diagnoseChamps):
    return sorted(diagnoseChamps.items(), key = lambda x: x[1]["wins"] + x[1]["losses"], reverse = True)[:3]

#Need to edit this by adding a conditional if not it is useless (will only show 100% rarely played champs)
#Returns a list of top 5 highest winrate champions (note that its only accurate when run against alot of matches)
def getTop5Champions(diagnoseChamps):
    return sorted(diagnoseChamps.items(), key = lambda x: float(x[1]["wins"]/(x[1]["wins"] + x[1]["losses"])), reverse = True)[:5]

"""

To get Traits stats

"""

#Returns a dictionary of Traits with number of wins and losses for each trait respectively
def diagnoseTraits(results):
    traits = {}
    for row in results:
        for trait in row[2]:
            #Only if trait is activated
            if trait["tier_current"] >= 1:
                if row[0] == True:
                    if trait["name"] not in traits:
                        traits[trait["name"]] = {"wins":1,"losses":0}
                    else:
                        traits[trait["name"]]["wins"] += 1
                else:
                    if trait["name"] not in traits:
                        traits[trait["name"]] = {"wins":0,"losses":1}
                    else:
                        traits[trait["name"]]["losses"] += 1
    return traits
#Returns a list of the top 3 most played traits
def getFavouriteTraits(diagnoseTraits):
    return sorted(diagnoseTraits.items(), key = lambda x: x[1]["wins"] + x[1]["losses"], reverse = True)[:3]

#Returns a list of top 5 highest winrate traits (note that its only accurate when run against alot of matches)
def getTop5Traits(diagnoseTraits):
    return sorted(diagnoseTraits.items(), key = lambda x: float(x[1]["wins"]/(x[1]["wins"] + x[1]["losses"])), reverse = True)[:5]

"""

To get Item Stats

"""

#Returns a list of items and the number of matches it was used in 
def getFavouriteItems(results):
    items = {}
    for row in results:
        for champion in row[3]:
            for item in champion["itemNames"]:
                if item not in items:
                    items[item] = 1
                else:
                    items[item] += 1
    return sorted(items.items(), key = lambda x: x[1], reverse = True)[:3]



# #Test Cases
# my_region = 'na1'

# puuid = get_puuid("lawlsoevers",my_region)

# match_History = get_MatchHistory(puuid,my_region,100)

# personal_Games = diagnoseGames(puuid,my_region,match_History)
# diagnosedChamps = diagnoseChampions(personal_Games)

# diagnosedTraits = diagnoseTraits(personal_Games)

# print(getTop5Traits(diagnosedTraits))

# print(getFavouriteTraits(diagnosedTraits))

# print(getTop5Champions(diagnosedChamps))

# print(getFavouriteChamps(diagnosedChamps))

# print(getFavouriteItems(personal_Games))