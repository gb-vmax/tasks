# Bug Report

### Describe the bug

The `aliasedSitePath` function is generating incorrect paths. When I pass in a file path and site directory, the resulting aliased path has the path segments reversed, making it point to the wrong location.

### Reproduction

```js
const filePath = '/some/path/to/website/docs/foo.md';
const siteDir = '/some/path/to/website';

const result = aliasedSitePath(filePath, siteDir);
console.log(result);
// Output: @site/../../../docs/foo.md
// Expected: @site/docs/foo.md
```

The function is producing paths with `../` segments going in the wrong direction instead of a clean relative path from the site directory.

### Expected behavior

The aliased path should be `@site/docs/foo.md` when the file is located at `docs/foo.md` relative to the site directory. The `@site` alias should correctly represent the site root, not generate paths that navigate upward with `../`.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
