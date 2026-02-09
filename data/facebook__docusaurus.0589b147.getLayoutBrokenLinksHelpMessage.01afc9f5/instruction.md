# Bug Report

### Describe the bug

When Docusaurus detects broken links that appear frequently across multiple pages (likely in layout components like navbar/footer), the help message displayed to users is corrupted and missing characters at the beginning of several lines.

### Reproduction

1. Create a Docusaurus site with broken links in the navbar or footer that appear on multiple pages (at least 6+ pages)
2. Build the site
3. Observe the broken links error message

The error message should provide helpful guidance about checking layout components, but instead shows garbled text like:

```
  looks like some of the broken links we found appear in many pages of your site.
 ybe those broken links appear on all pages through your site layout?
  recommend that you check your theme configuration for such links (particularly, theme navbar and footer).
 equent broken links are linking to:...
```

### Expected behavior

The message should be properly formatted and readable:

```
It looks like some of the broken links we found appear in many pages of your site.
Maybe those broken links appear on all pages through your site layout?
We recommend that you check your theme configuration for such links (particularly, theme navbar and footer).
Frequent broken links are linking to:...
```

This makes it difficult to understand what action needs to be taken to fix the broken links issue.

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
