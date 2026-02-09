# Bug Report

### Describe the bug

The `aliasedSitePath` function is returning incorrect paths when converting absolute file paths to `@site` aliased paths. Instead of generating paths like `@site/docs/foo.md`, it's producing malformed paths that don't resolve correctly.

### Reproduction

```js
const { aliasedSitePath } = require('@docusaurus/utils');

const siteDir = '/home/user/website';
const filePath = '/home/user/website/docs/foo.md';

const result = aliasedSitePath(filePath, siteDir);
console.log(result);
// Expected: @site/docs/foo.md
// Actual: incorrect path
```

### Expected behavior

When given a file path within the site directory, `aliasedSitePath` should return a proper `@site` aliased path that webpack can resolve. For example:
- Input: `/home/user/website/docs/foo.md` with siteDir `/home/user/website`
- Expected output: `@site/docs/foo.md`

### System Info
- Docusaurus version: latest
- Node version: 18.x

This is breaking module resolution in my Docusaurus project. The aliased paths are not being resolved correctly by webpack.

---
Repository: /testbed
