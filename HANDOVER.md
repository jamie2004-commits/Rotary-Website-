# Rotary Club of Jurong Town, Singapore
## Website handover

This folder is the entire website. There is no database, no platform account,
no plugins and nothing that expires. If everything else is lost, uploading this
folder to any static host brings the site back exactly as it was.

---

## 1. Publish it

**Fastest look, no account needed.** Go to app.netlify.com/drop and drag the
`site` folder onto the page. You get a live link in about ten seconds. Good for
showing the club. Use the proper option below for the real domain.

**The real one, free, Cloudflare Pages.**

1. Sign up at cloudflare.com using a club address, not a personal one.
2. Dashboard, then Workers and Pages, then Create, then Pages, then Upload assets.
3. Drag the `site` folder in. Name the project something like `rcjt-website`.
4. You get an address ending in `.pages.dev`. The site is live there.
5. Send that link to the club for review. Nothing has touched the current
   website at this point.
6. When approved: in the Pages project, Custom domains, add the club domain,
   then follow the instructions to point the domain at it. HTTPS is automatic
   and free.

To publish a change later, repeat step 3. Every upload is kept, so a bad change
can be rolled back with one click.

---

## 2. Two things to do before the domain switch

**Turn the forms on.** Both forms are wired but need a free key.

1. Go to web3forms.com, enter the club enquiry address, and they email a key.
2. Open `site/join/index.html` and `site/contact/index.html`, find
   `REPLACE_WITH_ACCESS_KEY`, and paste the key in place of it. Two files, one
   change each.
3. Send a test message through each form and confirm it arrives.

Use a club role address, never a personal one, or enquiries stop arriving the
day that person leaves the committee. The free plan covers 250 messages a
month, which is far more than this site will see.

**Back up the old site.** Take a full WordPress backup and export the media
library before pointing the domain anywhere. The current site has photographs
going back to 2016 that are worth keeping, and several of them can fill the
image slots described below.

---

## 3. What the club still needs to supply

Nothing here blocks publishing. The site is complete and readable without any
of it, but each one makes it better.

| Item | Where | Note |
|---|---|---|
| Photographs | Every page | See `site/img/README.txt`. Slots currently show a plain brand panel |
| Club logo | Header and favicon | Replace the placeholder mark with the club's own logo file |
| Leadership names | About page | Section is written and commented out, ready to switch on |
| Membership brochure | Join page | Link is written and commented out |
| Annual fee figure | Join page | Currently says "a modest annual fee", which matches the old site. Publishing the number is better than making people ask |
| Privacy notice details | Privacy page | Two items marked TO CONFIRM. The PDPA requires a named contact |
| Tax deductibility | Partner page | Only if the club wants to invite donations |

The Partner page is new. Nothing equivalent existed on the old site, so the
board should confirm it wants those three channels and who handles each. If
not, delete the `site/partner/` folder and remove the nav and footer links.

---

## 4. Making changes

Each page is one file. Open it in any text editor, find the words, change them,
save, re-upload. The design lives in `site/assets/style.css` and does not need
to be touched to edit text.

```
site/index.html          Home
site/about/index.html    About us
site/projects/index.html What we do
site/youth/index.html    Youth
site/join/index.html     Join us
site/partner/index.html  Partner
site/contact/index.html  Contact
site/privacy/index.html  Privacy notice
site/assets/style.css    The design, all of it
site/assets/site.js      Mobile menu and the next meeting date
site/_redirects          Sends old page addresses to the new ones
```

The next meeting date on the home page calculates itself from the 2nd and 4th
Tuesday rule. Nobody needs to update it. If the club ever changes its meeting
pattern, the rule is at the bottom of `site/assets/site.js`.

**Before anyone rebuilds this:** the site is hand-built HTML, not a template.
Moving it into a page builder, a theme or a club management platform will lose
the design. If a future committee wants changes, editing these files is far
cheaper than starting again.

---

## 5. Accounts to hold in the club's name

Static files do not decay. Accounts do. This is the part that determines
whether the site survives the next handover.

- [ ] Domain registration in the club's name, auto-renew on
- [ ] Cloudflare account on a club address
- [ ] Web3Forms account on a club address
- [ ] All three logins in the club's password manager
- [ ] At least two current officers with access
- [ ] A copy of this folder in the club's shared drive, kept separate from the
      hosting account

---

## 6. What was changed from the draft

- The single review file became seven real pages, so each has its own web
  address, title and description, and can be shared or found in search.
- The review banner, gold highlighting and internal placeholder index were
  removed.
- The member count was removed rather than guessed at.
- The forms now actually send. They previously did nothing.
- Old WordPress addresses now forward to the new pages, so existing links and
  search results keep working.
- Added a privacy notice, a custom page-not-found page, a sitemap and a
  favicon.
- Image placeholders became plain brand panels, so the site looks finished
  before the photographs arrive.

Every word of content came from the club's existing website. Nothing was
invented.
