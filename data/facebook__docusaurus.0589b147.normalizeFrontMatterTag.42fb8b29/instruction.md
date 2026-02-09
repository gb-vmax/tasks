# Bug Report

### Describe the bug

I'm experiencing an issue with tag permalink generation in my Docusaurus site. After a recent update, tags are no longer generating proper permalinks. Instead of getting normalized URL paths like `/tags/my-tag`, the permalinks appear to be broken or incorrectly formatted.

### Reproduction

```js
// In a blog post or doc with frontmatter:
---
tags:
  - label: My Tag
    permalink: custom-tag
---

// The tag permalink is not being normalized correctly
// Expected: /blog/tags/custom-tag
// Actual: broken/malformed permalink
```

When I use tags with custom permalinks in my frontmatter, they don't resolve to the correct paths anymore. The tag pages either don't load or the links are completely wrong.

### Expected behavior

Tags should generate normalized permalinks that include the proper base path (like `/blog/tags/` or `/docs/tags/`) and handle the permalink normalization correctly. Custom tag permalinks should work as they did before.

### Additional context

This seems to affect both simple string tags and object-style tags with custom permalinks. The issue appeared after updating to the latest version.

---
Repository: /testbed
