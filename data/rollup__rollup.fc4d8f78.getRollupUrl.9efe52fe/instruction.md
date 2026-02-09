# Bug Report

### Describe the bug

The `getRollupUrl` function is generating malformed URLs with double slashes. When I try to use the generated URLs, they don't work correctly.

### Reproduction

```js
import { getRollupUrl } from './utils/url';

const url = getRollupUrl('guide/introduction');
console.log(url);
// Output: https://rollupjs.org//guide%2Fintroduction
// Expected: https://rollupjs.org/guide/introduction
```

The URL has two issues:
1. Double slash after the domain (`//` instead of `/`)
2. The snippet is being URL encoded when it shouldn't be (forward slashes are converted to `%2F`)

### Expected behavior

The function should return a properly formatted URL like `https://rollupjs.org/guide/introduction` without double slashes or unnecessary encoding of the path.

### System Info
- Node version: 18.x
- Browser: Firefox 121

---
Repository: /testbed
