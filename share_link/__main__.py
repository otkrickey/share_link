from .bot import ShareLinkClient
from .cogs.share import ShareLink
from .task_manager import TaskManager


def main():
    manager = TaskManager()
    client = ShareLinkClient()
    client.add_cogMeta(ShareLink)

    loop = manager.get_loop()
    loop.create_task(client.run_bot())

    manager.start()

if __name__ == "__main__": main()