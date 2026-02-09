# Bug Report

### Describe the bug

Anchor links in Docusaurus are being incorrectly reported as broken when they actually exist on the target page. After a recent update, the broken links checker seems to have inverted logic and is flagging valid anchor links as broken while potentially missing actual broken anchors.

### Reproduction

1. Create a markdown page with an anchor/heading:
```md
## My Section
Some content here
```

2. Link to that anchor from another page:
```md
[Link to section](/docs/page#my-section)
```

3. Build the site

### Expected behavior

The link should be recognized as valid since the anchor exists on the target page. The broken links checker should not report it as broken.

### Actual behavior

Valid anchor links are being reported as broken links during the build process, even though the anchors clearly exist on the referenced pages.

This seems to affect all anchor links that point to existing sections/headings on pages that exist in the site.

---
Repository: /testbed
