#!python3
from os import mkdir
from os.path import isdir, join

from fbchat import Client
from fbchat.models import ImageAttachment
import urllib3

http = urllib3.PoolManager()


def download_pictures(user, password, thread_id, output_folder, msg_limit=100):
    if not isdir(output_folder):
        mkdir(output_folder)

    client = Client(user, password)

    msg_list = client.fetchThreadMessages(thread_id=thread_id, limit=msg_limit)
    for msg in msg_list:
        for att in msg.attachments:
            if not type(att) == ImageAttachment:
                continue
            url = client.fetchImageUrl(att.uid)
            data = http.request("GET", url=url, preload_content=False)
            data = data.read()
            output_filename = join(output_folder, att.uid + "." + att.original_extension)
            print("Downloading %s" % output_filename)
            with open(output_filename, "wb") as f:
                f.write(data)


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument("email", help="Email of your facebook account")
    parser.add_argument("password", help="Password of your facebook account")
    parser.add_argument("thread_id", help="ID of your conversation")
    parser.add_argument("--output", '-o', help="Output folder where pictures will be stored", default="./pictures")
    parser.add_argument('--limit', "-l", help="Limit on the number of messages to search for pictures", default=100)

    args = parser.parse_args()
    download_pictures(args.email, args.password, args.thread_id, args.output, args.limit)