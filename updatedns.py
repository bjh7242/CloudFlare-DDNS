#!/usr/bin/python3

import json
import requests

def read_config():
    with open('config.json','r') as f:
        config_info = f.read()
    return json.loads(config_info)
    

def get_record():
    headers = {'Authorization': apitoken, 'Content-Type': 'application/json', 'X-Auth-Key': apikey, 'X-Auth-Key': email}
    resp = requests.get("https://api.cloudflare.com/client/v4/zones/%s/dns_records" % zoneid, headers=headers)
    records = json.loads(resp.content.decode())

    for rec in records['result']:
        if rec['name'] == config['recordname']:
            return rec


def get_my_ip():
    resp = requests.get("https://api.ipify.org?format=json")
    ip = json.loads(resp.content.decode())['ip']
    return ip


def update_record():
    headers = {'Content-Type': 'application/json', 'X-Auth-Key': apikey, 'X-Auth-Email': email}
    rec_info = get_record()
    rec_type = rec_info['type']
    rec_id = rec_info['id']
    rec_ttl = rec_info['ttl']
    rec_name = rec_info['name']
    proxied = rec_info['proxied']
    newip = get_my_ip()

    data = {'type': rec_type, 'name': rec_name, 'content': newip, 'ttl': rec_ttl, 'proxied': proxied}
    resp = requests.put("https://api.cloudflare.com/client/v4/zones/%s/dns_records/%s" % (zoneid, rec_id), headers=headers, data=json.dumps(data))
    print(json.dumps(json.loads(resp.content.decode()), sort_keys=True, indent=4))
    


if __name__ == '__main__':
    config = read_config()
    zoneid = config['zoneid']
    apitoken = config['apitoken']
    apikey = config['apikey']
    email = config['authemail']
    recordname = config['recordname']
    update_record()

