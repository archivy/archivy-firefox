archivy-hn allows you to download your Firefox bookmarks into your [Archivy](https://archivy.github.io) knowledge base. 

It is an official extension developed by [archivy](https://github.com/archivy/).

## Install

You need to have [`archivy`](https://archivy.github.io) already installed.

Run `pip install archivy_firefox` (or `pip3`). 

## Usage

This plugin takes one argument: the location of the JSON export of your Firefox bookmarks. To get this, open the manage bookmarks view (Bookmarks > Manage Bookmarks, or `CTRL+SHIFT+O`), and then click Import and Backup > Backup...

Then run `archivy firefox EXPORT_LOCATION`.


```
$ archiv firefox --help
Usage: archivy firefox [OPTIONS] EXPORT_FILE

  Pull your upvoted or favorited posts from Hacker News and save their
  contents into your knowledge base

Options:
  --help  Show this message and exit.
```

## Contributing

You can open any issues or feature requests [here](https://github.com/archivy/archivy_hn/issues).

You can also talk to us directly on the [Archivy discord server](https://discord.gg/uQsqyxB)

## Improvement Ideas

- implement an ignore list - allowing you to not save specific links or folders
- parse directly from Firefox data (without needing user to export)? Not sure how easy this is.
