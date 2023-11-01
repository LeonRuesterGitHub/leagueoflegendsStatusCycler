
import requests
import json
import warnings
import time
warnings.simplefilter('ignore',lineno=1100)
from requests.auth import HTTPBasicAuth

print("starting...")
lollockfile = open("C:\Riot Games\League of Legends\lockfile").readline().split(":")
wmotjson = json.load(open("WMO.json"))
port = lollockfile[2]
password = lollockfile[3]

def wmotodescription (wmoindex):
    return wmotjson[wmoindex]["night"]["description"]

def getWeatherForRegion(latitude, longitude):
    response_API = requests.get('https://api.open-meteo.com/v1/forecast?latitude=' + latitude + '&longitude=' + longitude + '&current=temperature_2m,weathercode,relativehumidity_2m')
    json_object = json.loads(response_API.text)
    json_formatted_str = json.dumps(json_object, indent=2)
    out =  wmotodescription(str(json_object["current"]["weathercode"])) + " at " + str(json_object["current"]["temperature_2m"]) + "°C"
    print(out)
    return out

def setStatusMessage(message):
    payload = '{"availability":"online","gameName":"Gl4zy","gameTag":"EUW","icon":6298,"id":"e62c05cf-ddb7-5888-a506-337eda32bf3c@eu1.pvp.net","lastSeenOnlineTimestamp":null,"lol":{"bannerIdSelected":"1","challengeCrystalLevel":"PLATINUM","challengePoints":"13065","challengeTitleSelected":"6e291d4d-a730-d2e0-c127-0ef0416c2977","challengeTokensSelected":"","championId":"","companionId":"8010","damageSkinId":"47003","gameQueueType":"","gameStatus":"outOfGame","iconOverride":"","level":"487","mapId":"","mapSkinId":"65","masteryScore":"519","puuid":"e62c05cf-ddb7-5888-a506-337eda32bf3c","rankedLeagueDivision":"","rankedLeagueQueue":"","rankedLeagueTier":"","rankedLosses":"0","rankedPrevSeasonDivision":"IV","rankedPrevSeasonTier":"DIAMOND","rankedSplitRewardLevel":"0","rankedWins":"47","regalia":"{\\"bannerType\\":2,\\"crestType\\":1,\\"selectedPrestigeCrest\\":14}","skinVariant":"","skinname":""},"name":"Gl4zy","obfuscatedSummonerId":0,"patchline":"live","pid":"e62c05cf-ddb7-5888-a506-337eda32bf3c@eu1.pvp.net","platformId":"EUW1","product":"league_of_legends","productName":"","puuid":"e62c05cf-ddb7-5888-a506-337eda32bf3c","statusMessage":"'+ message +'","summary":"","summonerId":38506903,"time":0}'
    response_API = requests.put('https://127.0.0.1:' + port + '/lol-chat/v1/me', auth=HTTPBasicAuth('riot', password), verify=False, data=payload.encode())
    print("status has been set to: " + message)

def cycleStatusMessages(messages, interval=10):
    while True:
        
        
        for m in messages:
            setStatusMessage(m)
            time.sleep(interval)

        messages = []

        BerlinWeather = "Berlin: " + getWeatherForRegion("52.5244", "13.4105") 
        StuttgartWeather = "Stuttgart: " + getWeatherForRegion("48.7775", "9.1800")
        MunichWeather = "Munich: " + getWeatherForRegion("48.1375", "11.5750")
        HamburgWeather = "Hamburg: " + getWeatherForRegion("53.5500", "10.0000")
        CologneWeather = "Cologne: " + getWeatherForRegion("50.9364", "6.9528")
        FrankfurtWeather = "Frankfurt: " + getWeatherForRegion("50.1155", "8.6842")

        messages.append(BerlinWeather)
        messages.append(StuttgartWeather)
        messages.append(MunichWeather)
        messages.append(HamburgWeather)
        messages.append(CologneWeather)
        messages.append(FrankfurtWeather)

print("connecting to client at: " + port + ":" + password)
messages = []

BerlinWeather = "Berlin: " + getWeatherForRegion("52.5244", "13.4105") 
StuttgartWeather = "Stuttgart: " + getWeatherForRegion("48.7775", "9.1800")
MunichWeather = "Munich: " + getWeatherForRegion("48.1375", "11.5750")
HamburgWeather = "Hamburg: " + getWeatherForRegion("53.5500", "10.0000")
CologneWeather = "Cologne: " + getWeatherForRegion("50.9364", "6.9528")
FrankfurtWeather = "Frankfurt: " + getWeatherForRegion("50.1155", "8.6842")

messages.append(BerlinWeather)
messages.append(StuttgartWeather)
messages.append(MunichWeather)
messages.append(HamburgWeather)
messages.append(CologneWeather)
messages.append(FrankfurtWeather)

#messages = ["Ever on and on", "I continue circling", "With nothing but my hate", "In a carousel of agony", "'Til slowly I forget and my heart starts vanishing", "And suddenly I see that I can't", "Break free, I'm", "Slipping through the cracks of a dark eternity", "With nothing but my pain and a paralyzing agony", "To tell me who I am! Who I was!", "Uncertainty enveloping my mind", "'Til I can't break free, and", "Maybe it's a dream, maybe nothing else is real", "But it wouldn't mean a thing if I told you how I feel", "So I'm tired of all the pain, all the misery inside", "And I wish that I could live feeling nothing but the night", "You could tell me what to say, you could tell me where to go", "But I doubt that I would care, and my heart would never know", "If I make another move, there'll be no more turning back", "Because everything would change, and it all would fade to black", "Will tomorrow ever come? Will I make it through the night?", "Will there ever be a place for the broken in the light?", "Am I hurting? Am I sad? Should I stay or should I go?", "I've forgotten how to tell, did I ever even know?", "Can I take another step? I've done everything I can", "All the people that I see, they will never understand", "If I find a way to change, if I step into the light", "Then I'll never be the same and it all will fade to white", "Ever on and on", "I continue circling", "With nothing but my hate", "In a carousel of agony", "'Til slowly I forget and my heart starts vanishing", "And suddenly I see that I can't", "Break free, I'm", "Slipping through the cracks of a dark eternity", "With nothing but my pain and a paralyzing agony", "To tell me who I am! Who I was!", "Uncertainty enveloping my mind", "'Til I can't break free, and", "Maybe it's a dream, maybe nothing else is real", "But it wouldn't mean a thing if I told you how I feel", "So I'm tired of all the pain, all the misery inside", "And I wish that I could live feeling nothing but the night", "You could tell me what to say, you could tell me where to go", "But I doubt that I would care, and my heart would never know", "If I make another move, there'll be no more turning back", "Because everything would change, and it all would fade to black", "Will tomorrow ever come? Will I make it through the night?", "Will there ever be a place for the broken in the light?", "Am I hurting, am I sad? Should I stay or should I go?", "I've forgotten how to tell, did I ever even know?", "This time you're not hurting me! This time I will take a stand!", "All the hatred in my eyes building up an evil plan", "Standing lonely in the night, with the darkness by my side", "Looking deep inside myself, and revealing only fright", "If I make another move, if I take another step", "Then it would all fall apart, there'd be nothing of me left", "If I'm crying in the wind, if I'm crying in the night", "Will there ever be a way? Will my heart return to white?", "Can you tell me who you are? Can you tell me where I am?", "I've forgotten how to see, I've forgotten if I can", "If I open up my eyes, there'll be no more going back", "'Cause I'll throw it all away, and it all will fade to black", "So I'm back here once again, so I'm back here once again", "Can I ever make a change? Will my heart begin to mend?", "Would you love me if I go? It feels like a heart attack", "But still everything's the same, and it all just fades to black"]

cycleStatusMessages(messages, 10)
