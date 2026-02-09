# Bug Report

### Broken links detection message is corrupted

I'm seeing a strange issue with the broken links detection feature. When Docusaurus detects broken links that appear frequently across multiple pages, the help message that's supposed to guide users is getting corrupted.

### Reproduction

1. Create a site with broken links that appear on multiple pages (e.g., a broken link in the navbar or footer)
2. Build the site
3. Look at the broken links error message

The message that's supposed to say something like:

```
It looks like some of the broken links we found appear in many pages of your site.
Maybe those broken links appear on all pages through your site layout?
We recommend that you check your theme configuration for such links (particularly, theme navbar and footer).
Frequent broken links are linking to: [links]
```

Instead shows up with missing characters at the beginning of each line:

```
  looks like some of the broken links we found appear in many pages of your site.
 ybe those broken links appear on all pages through your site layout?
  recommend that you check your theme configuration for such links (particularly, theme navbar and footer).
 equent broken links are linking to: [links]
```

The first few characters of each line are missing ("It", "Ma", "We", "Fr"), making the message harder to read and understand.

### Expected behavior

The help message should display correctly with all characters intact to properly guide users in fixing their broken links.

---
Repository: /testbed
