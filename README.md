# Mastofeed

A scraper+viewer for Mastodon user feeds

This repo isn't really set up to be used out of the box. You'll need to update the file paths in `archive.py` and `view.py`, as I had those hard coded to my personal directories so I can alias them and not have to worry about it breaking.

You will also need to create the following files in the root directory:
- `archived.txt`
- `data.txt`
- `following.txt`

To add a mastodon user, edit `following.txt` and put their account in the following format, one per line:
```
username@domain.tld
```

You can then manually run `scrape.py` to fetch posts. I set up a cron job to run it every 15 minutes.

When scrape runs, it adds a post per line to the `data.txt` file

To view posts in data.txt, you can run `view.py`, which will format and output them in ascending order.

You can either manually move posts from that file over to archive.txt so they no longer appear when running `view.py`, or you can archive everything in `data.txt` by running `archive.py`.

I'm sure this could be better, but this fit my needs. Feel free to fork it and modify it however works for you!
