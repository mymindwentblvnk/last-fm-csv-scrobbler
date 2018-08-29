# last_fm_csv_scrobbler

## Setup

* `make venv`
* `cp rename_to_settings.py settings.py`
* Add API information to `settings.py`
    * You have to have your own unique two values for API_KEY and API_SECRET
    * Obtain yours from https://www.last.fm/api/account/create for Last.fm
* Create CSV files that you want to scrobble that hold the following information
    * Time (UTC timestamp) when the song was played
    * Track title
    * Artist name
    * Album name (optional)
* Add CSV file information to `settings.py`
    * You can add as many CSV files as you want
    * You have to add information about where the needed information can be found in the CSV file
        * Column name of track title column
        * Column name of timestamp column
        * Column name of artist name column
        * Column name of album name column

If you want to scrobble Songs from an old Last.fm account you can create CSV files of this account with services like [Last.fm to CSV](https://benjaminbenben.com/lastfm-to-csv/) of [benfoxall](https://github.com/benfoxall/lastfm-to-csv) or [Last.fm data export](https://mainstream.ghan.nl/export.html) of [ghan64](https://www.last.fm/user/ghan64/shoutbox)

## Run script
`make process`
