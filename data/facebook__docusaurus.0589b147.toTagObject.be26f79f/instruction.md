# Bug Report

### Describe the bug

When using tags in front matter, the tag label is being converted to kebab-case instead of preserving the original string. This causes the displayed tag labels to appear in kebab-case format (e.g., "my-tag" instead of "My Tag") which is not the expected behavior.

### Reproduction

```js
// In a blog post or doc with front matter:
---
tags: ['My Custom Tag', 'Another Tag']
---

// Expected: Tag labels show as "My Custom Tag" and "Another Tag"
// Actual: Tag labels show as "my-custom-tag" and "another-tag"
```

### Expected behavior

The tag label should preserve the original string from the front matter, while only the permalink should be converted to kebab-case. For example:
- Label: "My Custom Tag"
- Permalink: "my-custom-tag"

Currently both the label and permalink are being set to kebab-case versions of the string.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
