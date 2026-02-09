# Bug Report

### Describe the bug

The `aliasedSitePath` function is returning incorrect paths. Instead of converting absolute file paths to site-relative paths with the `@site` alias prefix, it's producing malformed paths with `@site` appended at the end.

### Reproduction

```js
import {aliasedSitePath} from '@docusaurus/utils';

const siteDir = '/home/user/website';
const filePath = '/home/user/website/docs/foo.md';

const result = aliasedSitePath(filePath, siteDir);
console.log(result);
// Current output: /home/user/website/docs/foo.md/@site
// Expected output: @site/docs/foo.md
```

The function should convert absolute paths to site-relative paths prefixed with `@site/`, but it's currently:
1. Resolving to an absolute path instead of computing a relative path
2. Appending `/@site` at the end instead of prefixing with `@site/`

### Expected behavior

The function should return `@site/docs/foo.md` when given `/home/user/website/docs/foo.md` as the file path and `/home/user/website` as the site directory. The `@site` alias should be at the beginning of the path, not the end.

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
