# Bug Report

### Describe the bug

When using tags in front matter, the permalink generation seems broken. Tags are not generating the correct permalink paths - they're missing the base tags path prefix.

### Reproduction

```js
// In front matter:
tags:
  - tutorial
  - guide

// Expected permalink: /tags/tutorial
// Actual permalink: tutorial (missing /tags/ prefix)
```

When I define tags as strings in the front matter, the generated permalinks are just the kebab-cased tag names without the proper path prefix. This breaks tag navigation since the links don't include the `/tags/` base path.

### Expected behavior

Tag permalinks should include the full path with the tags base path (e.g., `/tags/tutorial` instead of just `tutorial`). The normalization should handle both string tags and object tags consistently.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
