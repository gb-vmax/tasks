# Bug Report

### Describe the bug

I'm experiencing an issue with broken link detection where valid internal links are being incorrectly flagged as broken links. It seems like the logic for determining whether a pathname matches a route has been inverted somehow.

### Reproduction

```js
// Given a site with the following routes:
// - /docs/intro
// - /blog/welcome
// - /about

// When checking links:
const validLink = '/docs/intro';
const brokenLink = '/nonexistent-page';

// Expected: validLink should NOT be flagged as broken
// Actual: validLink IS flagged as broken

// Expected: brokenLink SHOULD be flagged as broken  
// Actual: brokenLink is NOT flagged as broken
```

### Expected behavior

- Valid links that match existing routes should pass validation
- Invalid links that don't match any routes should be detected as broken
- The broken links checker should correctly identify which links are valid vs broken

### Additional context

This appears to affect all internal link validation. The behavior is completely reversed from what it should be - valid links are treated as broken and broken links are treated as valid.

---
Repository: /testbed
