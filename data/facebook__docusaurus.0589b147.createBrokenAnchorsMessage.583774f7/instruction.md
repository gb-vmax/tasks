# Bug Report

### Describe the bug

The broken anchors validation is not working correctly - when there are broken anchors in the documentation, no warning or error message is displayed. The validation seems to be completely silent even when anchors are broken.

### Reproduction

1. Create a documentation page with a link to an anchor that doesn't exist
2. Build the site with `onBrokenAnchors` set to 'warn' or 'throw'
3. Observe that no broken anchor messages are shown

Example:
```md
<!-- docs/page1.md -->
[Link to non-existent anchor](#this-anchor-does-not-exist)
```

```js
// docusaurus.config.js
module.exports = {
  onBrokenAnchors: 'warn',
  // ...
}
```

### Expected behavior

When broken anchors are detected, the build process should display a warning or error message listing all the broken anchors found, similar to how broken links are reported.

The message should include:
- Which pages contain broken anchors
- What anchors are broken
- Where they are referenced from

### System Info

- Docusaurus version: latest
- Node version: 18.x
- OS: macOS

---
Repository: /testbed
