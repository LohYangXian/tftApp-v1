""" Functions to be created:

We need a Front-end UI package similar to Tkinter

Features of the UI

Input
- Select Region
- Key in Summoner Name

Output

Displays Summoner's 

1) Favourite Champions
2) Favourite Items
3) Favourite Traits
Return to Search Bar Button

"""

"""
Functions to be created:
1) File to store the API Key [ Done ]
2) get_SummonerID(Summoner Name, Region) : Returns Summoner ID number [ Done ]
e.g.
https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/lawlsoevers
then ["id"] the result
["puuid"] to get Puuid (more universal id string)

3) get_Rank(SummonerID) [Done]
e.g.
https://na1.api.riotgames.com/tft/league/v1/entries/by-summoner/6w44gCqoB83VOc0xzYdBH2JMHa1B_oMzDbBv-I70OkKdvEJqkATNF8jLHg
then ["tier"] for tier and ["rank"] for rank

4) get_MatchIDS(puuid) [Done]
e.g.
https://americas.api.riotgames.com/tft/match/v1/matches/by-puuid/oAzOnlcaESQrc67c3d9xeUZZJPOq8nidjWcbPjz9J7408HwX5_zys_H2Mvwh-kURzbWmV_VWA2JP9w/ids?count=20

Returns a list of Strings of Match IDs

5) get_MatchInfo(MatchId) [Done]
e.g. 
https://americas.api.riotgames.com/tft/match/v1/matches/NA1_4301892796

To find Player Info, 
["info"]["participants"] -> List of dictionaries (Players' info) during the match
Loop through the list and check ["puuid"] matches the Player's puuid 
["augments"] -> List of the 3 Augments chosen during match
["placement"] -> Int of Positioning
["traits"] -> List of Dictionaries of Traits played (Could be unactivated (0))
["Units"] -> List of Disctionaries of Units played (Including Items equipped)



Note the Rate Limit for Development Key:
20 requests every 1 second
100 requests every 2 minutes

Problem is that most of the requests are made when gathering match information (1 request per match ID)

Find a way to add a timer between each query so that we do not exceed the rate limit. 

We should query matches and store the data in a local variable first, before looping through the information to do any analysis 

One Request is each time you access the URL

May/May not have to use RiotWatcher (You can code it yourself)

"""