Simple script to download all pictures from a facebook conversation
This script is using [fbchat](https://github.com/carpedm20/fbchat)

# Usage
```
usage: download_messenger_pictures.py [-h] [--output OUTPUT] [--limit LIMIT]
                                      email password thread_id

positional arguments:
  email                 Email of your facebook account
  password              Password of your facebook account
  thread_id             ID of your conversation

optional arguments:
  -h, --help            show this help message and exit
  --output OUTPUT, -o OUTPUT
                        Output folder where pictures will be stored
  --limit LIMIT, -l LIMIT
                        Limit on the number of messages to search for pictures
```