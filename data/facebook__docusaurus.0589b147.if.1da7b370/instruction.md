# Bug Report

### Describe the bug

When setting `onBrokenAnchors: 'ignore'` in the configuration, broken links checking is also being skipped even when `onBrokenLinks` is set to a different value like `'warn'` or `'throw'`. This means that broken links are not being reported when they should be.

### Reproduction

```js
// docusaurus.config.js
module.exports = {
  onBrokenLinks: 'throw',
  onBrokenAnchors: 'ignore',
  // ... other config
}
```

With this configuration:
1. Create a page with a broken link to another page (e.g., `[link](/nonexistent-page)`)
2. Build the site
3. Expected: Build should fail due to broken link
4. Actual: Build succeeds, broken link is not detected

The same issue occurs in reverse - setting `onBrokenLinks: 'ignore'` also causes `onBrokenAnchors` checking to be skipped.

### Expected behavior

The two settings should be independent:
- `onBrokenLinks: 'throw'` with `onBrokenAnchors: 'ignore'` should still check and report broken links
- `onBrokenLinks: 'ignore'` with `onBrokenAnchors: 'warn'` should still check and report broken anchors

Each setting should only control its respective validation type.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
