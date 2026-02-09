# Bug Report

### Describe the bug

Broken anchor link detection is not working correctly. When I have a link pointing to an anchor on a page that doesn't exist, it's not being reported as a broken link. The validation seems to be inverted - valid anchors are flagged as broken while actually broken anchors pass validation.

### Reproduction

```js
// Scenario 1: Link to non-existent anchor on existing page
// Expected: Should be reported as broken
// Actual: Not reported as broken
const link1 = { pathname: '/docs/intro', hash: '#non-existent-anchor' }

// Scenario 2: Link to valid anchor on existing page  
// Expected: Should NOT be reported as broken
// Actual: Reported as broken
const link2 = { pathname: '/docs/intro', hash: '#valid-anchor' }
```

The logic appears to be backwards - anchors that exist on the target page are being treated as broken, while anchors that don't exist are passing validation.

### Expected behavior

- Links to anchors that exist on a page should be valid (not broken)
- Links to anchors that don't exist on a page should be reported as broken links
- Links to anchors on pages that don't exist should be reported as broken links

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
