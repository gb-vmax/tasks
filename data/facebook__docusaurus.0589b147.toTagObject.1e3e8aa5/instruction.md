# Bug Report

### Describe the bug

When using tags in front matter, the tag label is being incorrectly transformed to kebab-case instead of preserving the original string. This breaks the display of tags that should maintain their original formatting.

### Reproduction

```js
// Front matter with a tag
const frontMatterTag = "My Custom Tag";

// After normalization
// Expected label: "My Custom Tag"
// Actual label: "my-custom-tag"
```

The tag label is being converted to kebab-case when it should preserve the original string value. Only the permalink should be transformed to a URL-friendly format.

### Expected behavior

- The `label` property should preserve the original tag string (e.g., "My Custom Tag")
- The `permalink` property should be the kebab-cased version (e.g., "my-custom-tag")

### Current behavior

Both `label` and `permalink` are being transformed to kebab-case, causing the original tag text to be lost.

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
