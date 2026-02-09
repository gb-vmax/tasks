# Bug Report

### Describe the bug

I'm experiencing an issue with broken link detection in Docusaurus where links without anchors/hash fragments are being incorrectly flagged as broken anchor links. 

When I have a regular link to a page (like `/docs/intro` or `/blog/my-post`) without any hash/anchor, the broken link checker is treating it as if it's a broken anchor link instead of recognizing it as a valid page link.

### Reproduction

```js
// Example links that are incorrectly flagged:
<Link to="/docs/getting-started">Guide</Link>
<a href="/blog/welcome">Blog Post</a>

// These are valid pages that exist, but they're being reported as broken
// because they don't have a hash fragment
```

### Expected behavior

Links without hash fragments should be validated as page links, not anchor links. The broken link checker should only validate anchor existence when a hash is actually present in the URL (e.g., `/docs/intro#installation`).

Regular page links like `/docs/intro` should pass validation if the page exists, regardless of whether they have an anchor or not.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
