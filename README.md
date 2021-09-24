# Crypto Trading Bot

## Local Development

You will need the following installed on your local machine:

-   Docker

Steps to get up and running

1. Run `make init` to spin up the docker container. Note you will automatically be "ssh'ed" into the main docker container from which you can run your python code.
2. To run application manually run `python app.py`.
3. Application will automatically run hourly via cron job (`crypto.crontab`) - cron runs are logged to `/var/log/cron.log`

-   Mysql data will persist to `storage/mysql_data` directory
-   The top 3 crypto currencies are stored in `top_crypto_currencies` table which will be updated hourly
-   Hourly trades are logged to `storage/logs/app.log` as well as to stderr
-   Errors are logged to `storage/logs/error.log` as well as to stderr

### Database Access

If you would like to access the database via a GUI such as Sequel Pro or Tableplus, you can use the following credentials:

Host: `127.0.0.1`
User: `docker`
Password: `secret`
Database: `crypto`
Port: `33060`
