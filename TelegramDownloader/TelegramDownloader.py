import json
from telethon import TelegramClient, client, events
from telethon.tl.types import InputMessagesFilterDocument, InputMessagesFilterVideo
from telethon.utils import get_display_name

class TelegramDownloader:
    def __init__(self, api_id, api_hash) -> None:
        self._api_id = api_id
        self._api_hash = api_hash
        self._client = TelegramClient("Downloader",
            self._api_id, self._api_hash)

    def run(self):
        with self._client:
            self._client.loop.run_until_complete(self._main())


    async def _main(self):
        #TODO: remove dialogs limit
        dialogs = await self._client.get_dialogs(43)

        for d in dialogs:
            name = get_display_name(d.entity)
            if name in ("Fumetsu No Anata E"):
                messages = self._client.iter_messages(name, filter=InputMessagesFilterDocument) #InputMessagesFilterVideo)
                async for msg in messages:
                    print(get_display_name(msg.sender))
                    if hasattr(msg, "message"):
                        print(msg.message)
                    print("---------------")


    def get_media(self, channel:str)->list:
        pass

if __name__=="__main__":
    # TODO: get api id and hash from condig file
    API_ID = "TELEGRAM_API_ID"
    API_HASH = "TELEGRAM_API_HASH"
    teldown = TelegramDownloader(API_ID, API_HASH)
    teldown.run()

    # TODO where is the script going to be executed
    # how to set path
    cfg_json_path = "./TelegramDownloader/config/channels.json"
    with open(cfg_json_path) as json_file:
        channels_cfg = json.load(json_file)
        print(channels_cfg)
