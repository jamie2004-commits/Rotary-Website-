# Rotary Club of Jurong Town, Singapore

The club website. Plain HTML and CSS, no framework, no build step, no database.

**Live site:** (add the address once the domain is connected)

## What is in here

```
site/                 The website. Everything in this folder is published
site/index.html       Home
site/about/           About us
site/projects/        What we do
site/youth/           Youth
site/join/            Join us
site/partner/         Partner
site/contact/         Contact
site/privacy/         Privacy notice
site/assets/style.css The design, all of it
site/assets/site.js   Mobile menu and the next meeting date
site/_redirects       Sends old page addresses to the new pages
site/img/             Photographs
site/fonts/           Optional self-hosted font files

HANDOVER.md           Read this first. Accounts, what is outstanding, how to edit
build.py              Optional. Regenerates the pages from one shared template
```

## How changes go live

Cloudflare Pages watches this repository. Any change committed to the `main`
branch is published automatically, usually within a minute. Nothing needs to be
uploaded by hand.

To edit a page without installing anything: open the file here on GitHub, click
the pencil icon, make the change, and click Commit changes. The live site
updates itself.

Every change is recorded with a date and an author, so anything can be undone.

## Build settings in Cloudflare

```
Framework preset:        None
Build command:           (leave empty)
Build output directory:  site
```

There is no build step. Cloudflare simply serves the `site` folder as it is.

## Before rebuilding this

The site is hand-built HTML, not a template. Moving it into a page builder, a
theme, or a club management platform will lose the design. Editing these files
is far cheaper than starting again.
