# Bug Report

### Describe the bug

Links that should be valid are being reported as broken, while actual broken links are not being detected. The broken link checker seems to be working in reverse - it's flagging valid internal links as errors and letting broken ones pass through.

### Reproduction

```js
// Given a site with these valid routes:
// - /docs/intro
// - /blog/hello
// - /about

// Valid links are incorrectly flagged as broken:
<Link to="/docs/intro">Intro</Link>  // ❌ Reported as broken
<Link to="/blog/hello">Blog</Link>   // ❌ Reported as broken

// While actual broken links pass validation:
<Link to="/does-not-exist">Invalid</Link>  // ✅ No error reported
```

### Expected behavior

The broken link checker should:
- Allow valid links that match existing routes
- Report errors for links that don't match any route

Currently it's doing the opposite.

### System Info
- Docusaurus version: Latest
- Node version: 18.x

This seems to have started happening recently. The broken link detection logic appears to be inverted somehow.

---
Repository: /testbed
