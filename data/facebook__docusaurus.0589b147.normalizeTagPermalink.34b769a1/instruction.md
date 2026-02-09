# Bug Report

### Describe the bug

When using custom permalinks for tags in versioned docs, the `tagsPath` is no longer being prepended to the tag permalink. This causes tags to be generated at incorrect URLs, breaking the tag page routing.

### Reproduction

```js
// In a versioned doc with front matter:
---
tags:
  - label: "My Tag"
    permalink: "/custom-tag"
---

// Expected URL: /docs/v1/tags/custom-tag
// Actual URL: /custom-tag
```

The tag pages are now generated without the proper base path, which means:
1. Tags from different doc versions can collide on the same URL
2. Tag pages don't follow the expected URL structure
3. Navigation to tag pages may fail or lead to wrong locations

### Expected behavior

Tag permalinks should respect the `tagsPath` parameter and prepend it to custom permalinks, maintaining the correct URL structure for versioned documentation. Tags with custom permalinks in v1/doc.md and v2/doc.md should lead to different pages as intended.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
