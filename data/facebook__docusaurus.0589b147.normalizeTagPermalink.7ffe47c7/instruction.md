# Bug Report

### Describe the bug

When using custom tag permalinks with a leading slash, the tag URL gets malformed. The `tagsPath` is being appended incorrectly, resulting in broken tag page links.

### Reproduction

```js
// Given a tagsPath like '/docs/tags'
// And a tag with a custom permalink like '/custom-tag'

const tag = {
  permalink: '/custom-tag'
}

// Expected URL: /docs/tags/custom-tag
// Actual URL: /custom-tag/docs/tags
```

The issue occurs when normalizing tag permalinks - the order of path segments gets reversed when the permalink starts with a slash.

### Expected behavior

Tags with custom permalinks should have the `tagsPath` prepended to them, not appended. For versioned docs, the version-specific tags path should be applied first, then the custom permalink should follow.

For example:
- tagsPath: `/docs/v1/tags`
- custom permalink: `/my-tag`
- expected result: `/docs/v1/tags/my-tag`

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
