# Bug Report

### Describe the bug

The broken links detection helper message is displaying incorrect information. When there are broken links that appear frequently across multiple pages (like in a navbar or footer), the message shows page paths instead of the actual broken link URLs.

### Reproduction

1. Create a Docusaurus site with a broken link in the navbar (e.g., `/nonexistent-page`)
2. Have this broken link appear on at least 5+ pages
3. Run the build command
4. Check the broken links error message

### Expected behavior

The helper message should display the actual broken link URLs that appear frequently, not the page paths where they appear. For example:

```
It looks like some of the broken links we found appear in many pages of your site.
Maybe those broken links appear on all pages through your site layout?
We recommend that you check your theme configuration for such links (particularly, theme navbar and footer).
Frequent broken links are linking to: /nonexistent-page
```

### Actual behavior

Instead, the message shows page paths like `/docs/intro`, `/blog/welcome`, etc., which doesn't help identify which links are actually broken.

Also noticed the message text seems corrupted with missing characters at the beginning of some lines ("looks like" instead of "It looks like", "ybe" instead of "Maybe", etc.).

This makes it really hard to debug broken links that appear site-wide through layouts/components.

---
Repository: /testbed
