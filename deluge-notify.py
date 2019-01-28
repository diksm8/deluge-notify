#!/usr/bin/env python2.7
import requests
import json
import click

token = ""


@click.command()
@click.argument("Torrent_ID")
@click.argument("Torrent_Name")
@click.argument("Torrent_Path")
@click.argument("Token", default=token)
def main(torrent_id, torrent_name, torrent_path, token):
    """Simple script to send notifications on torrent completion using
    pusbullet and deluge execute.
    """
    message = "%s downloaded to %s" % (
        torrent_name, torrent_path.split('/')[-1])
    data_send = {"type": "note",
                 "title": "Completed",
                 "body": message}
    headers = {'Authorization': 'Bearer ' + token,
               'Content-Type': 'application/json'}
    resp = requests.post('https://api.pushbullet.com/v2/pushes',
                         data=json.dumps(data_send), headers=headers)
    if resp.status_code != 200:
        raise Exception('Something wrong')
    else:
        print('Completed.')


if __name__ == '__main__':
    main()
