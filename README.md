# CloudFlare-DDNS
This script is designed to be run as a cron job on a system where you would like to dynamically update the DNS record with the public IP of the system running this.

## To install and configure
You will have to modify the config.json file and update it with the following information from the CloudFlare dashboard:
My Profile -> API Tokens tab
* Create "Edit Zone" API token -> this will replace the apitoken value "BBBBBBBBB-BBBBBBBBBBBBBBBBBBBBBBBBBBBBBB" in the config.json; DO NOT REMOVE "Bearer" FROM THIS VALUE IN THE CONFIG
* View Global API key -> this will replace the "apikey" value in the config.json file
* authemail -> this is the email address you use to log into the CloudFront dashboard
* zoneid -> can be obtained from the overview tab of your zone page where you manage DNS records

Modify your `config.json` file and execute the following commands to run the script as a cron job every hour.
```bash
cd /opt && git clone https://github.com/bjh7242/CloudFlare-DDNS
echo "0/60 * * * * root python3 /opt/CloudFlare-DDNS/updatedns.py" >> /etc/crontab
```
