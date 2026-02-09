# Bug Report

### Describe the bug

The `aliasedSitePath` function is generating incorrect paths with double slashes (`@site//`) instead of single slashes (`@site/`). This is causing issues with module resolution and file path references.

### Reproduction

```js
import { aliasedSitePath } from '@docusaurus/utils';

const siteDir = '/path/to/website';
const filePath = '/path/to/website/docs/foo.md';

const result = aliasedSitePath(filePath, siteDir);
console.log(result);
// Output: @site//docs/foo.md
// Expected: @site/docs/foo.md
```

### Expected behavior

The function should return paths with a single slash after `@site`, like `@site/docs/foo.md`, not `@site//docs/foo.md`.

### Additional context

This appears to be breaking module imports and file references that rely on the aliased site path format. The double slash is causing webpack and other tools to fail when trying to resolve these paths.

---
Repository: /testbed
