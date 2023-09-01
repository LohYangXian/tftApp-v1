from riotwatcher import TftWatcher, ApiError
# Insert TFT API Key here
apiKey = ""
tft_watcher = TftWatcher(apiKey)

def getApiKey():
    return tft_watcher


