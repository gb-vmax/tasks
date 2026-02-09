# Bug Report

### Describe the bug

The `aliasedSitePath` function is producing incorrect paths. Instead of generating the expected `@site/` prefixed relative path from the site directory to a file, it's returning malformed paths.

### Reproduction

```js
const { aliasedSitePath } = require('@docusaurus/utils');

const siteDir = '/path/to/website';
const filePath = '/path/to/website/docs/foo.md';

const result = aliasedSitePath(filePath, siteDir);
console.log(result);
// Expected: @site/docs/foo.md
// Actual: @site/../../docs/foo.md (or similar incorrect path)
```

### Expected behavior

The function should return a path like `@site/docs/foo.md` when given a file path within the site directory. The `@site/` alias should be followed by the relative path from the site directory to the file.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
