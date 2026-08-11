FONTS
=====

The site currently loads Open Sans from Google Fonts. It works, and you can
leave it as is.

To serve the font from this site instead (one less external request, and
nothing outside the site is contacted when someone visits):

1. Go to fonts.google.com/specimen/Open+Sans and download the family.
2. Convert to woff2 if the download is a ttf. Free converters are fine, or
   use fonttools: pyftsubset with --flavor=woff2
3. Put the file in this folder and name it: open-sans-variable.woff2
4. Open assets/style.css, find the block marked "Self-hosted fonts" near the
   top, and uncomment it.
5. In every .html file, delete the three <link> lines that mention
   fonts.googleapis.com and fonts.gstatic.com.
6. Re-upload the folder.

Open Sans is licensed under the SIL Open Font License, so hosting it this way
is permitted.
