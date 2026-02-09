# Bug Report

### Describe the bug

The `getEditUrl` function is not returning the correct edit URL anymore. When I provide an `editUrl` parameter, it returns `undefined` instead of the expected normalized URL with the file path appended.

### Reproduction

```js
import { getEditUrl } from '@docusaurus/utils';

const editUrl = 'https://github.com/myorg/myrepo/edit/main';
const filePath = 'docs/intro.md';

const result = getEditUrl(filePath, editUrl);
console.log(result); // Expected: 'https://github.com/myorg/myrepo/edit/main/docs/intro.md'
                     // Actual: undefined
```

### Expected behavior

When `editUrl` is provided, the function should return a normalized URL combining the base edit URL and the file path. Currently it's returning `undefined` when it should be returning the full URL.

### System Info

- @docusaurus/utils version: latest
- Node version: 18.x

---
Repository: /testbed
