IMAGES
======

Photographs go in this folder.

Every image slot on the site is a div with class "media". Until a photo is
added, it shows a plain brand-coloured panel so the page still looks finished.

To add a photograph, find the slot in the page file, for example in
index.html:

    <div class="media"></div>

and replace the whole line with:

    <img class="media" src="img/hero.jpg" alt="Members packing meals at ...">

On pages inside a folder (about, projects, and so on) the path needs to step
up one level:

    <img class="media" src="../img/project-happiness-fund.jpg" alt="...">

Notes
- The alt text is the short description read aloud to a visitor using a screen
  reader, and shown if the image fails to load. Write what is happening in the
  photo, not "photo".
- Save photographs at roughly 1600px wide and under 400KB. Large files make
  the site slow, especially on mobile data.
- Only use photographs the club has permission to publish. Ask before posting
  images of identifiable people, especially young people at Interact events.
