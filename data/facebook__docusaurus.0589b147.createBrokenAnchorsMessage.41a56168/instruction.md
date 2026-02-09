# Bug Report

### Describe the bug

When building a Docusaurus site with broken anchors, the broken anchor validation message is not being displayed correctly. The error message that should list all broken anchors on the site is not showing up even when there are broken anchor links present.

### Reproduction

1. Create a Docusaurus site with some pages containing anchor links
2. Add a broken anchor reference (e.g., `[link](#non-existent-anchor)`)
3. Build the site with broken anchor checking enabled
4. Expected error message listing broken anchors doesn't appear

For example:
```md
<!-- In docs/page1.md -->
# Page 1

[Go to section](#missing-section)

<!-- The anchor #missing-section doesn't exist -->
```

### Expected behavior

The build process should detect the broken anchor and display an error message like:

```
Docusaurus found broken anchors!

Please check the pages of your site in the list below, and make sure you don't reference any anchor that does not exist.
Note: it's possible to ignore broken anchors with the 'onBrokenAnchors' Docusaurus configuration, and let the build pass.

Exhaustive list of all broken anchors found:
- On source page path = /docs/page1:
   -> linking to /docs/page1#missing-section (anchor not found)
```

Instead, the validation seems to be skipped and no message is shown.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
