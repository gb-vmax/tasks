# Bug Report

### Describe the bug

I'm experiencing an issue where heading IDs in MDX files are not being escaped properly. When I have `mdx1Compat.headingIds` set to `false` in my Docusaurus config, the heading IDs are still being escaped, which is the opposite of what should happen.

Additionally, when `mdx1Compat.admonitions` is enabled, the preprocessing seems to stop early and doesn't process heading IDs at all, even when they should be processed.

### Reproduction

```js
// docusaurus.config.js
module.exports = {
  markdown: {
    mdx1Compat: {
      headingIds: false,
      admonitions: true
    }
  }
}
```

With this configuration:
1. When `headingIds` is `false`, heading IDs are still being escaped (should not escape)
2. When `admonitions` is `true`, heading ID processing is completely skipped

### Expected behavior

- When `mdx1Compat.headingIds` is `true`, heading IDs should be escaped
- When `mdx1Compat.headingIds` is `false`, heading IDs should NOT be escaped
- The `admonitions` setting shouldn't cause early return that skips heading ID processing

### System Info

- Docusaurus version: Latest
- Node version: 18.x

---
Repository: /testbed
