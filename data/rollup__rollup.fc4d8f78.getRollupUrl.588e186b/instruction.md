# Bug Report

### Describe the bug

The `getRollupUrl` function is generating malformed URLs with double slashes and using `http` instead of `https`. When I try to use the generated URL to link to Rollup documentation, it results in broken links.

### Reproduction

```js
import { getRollupUrl } from './utils/url';

const url = getRollupUrl('guide/en');
console.log(url);
// Outputs: http://rollupjs.org//guide/en
// Expected: https://rollupjs.org/guide/en
```

The generated URL has two issues:
1. Uses `http://` instead of `https://`
2. Has double slashes (`//`) after the domain

### Expected behavior

The function should generate valid HTTPS URLs with proper formatting:
- `getRollupUrl('guide/en')` should return `https://rollupjs.org/guide/en`
- Links should be secure (https) and properly formatted

### System Info
- Node version: 18.x
- Browser: Firefox 121

---
Repository: /testbed
