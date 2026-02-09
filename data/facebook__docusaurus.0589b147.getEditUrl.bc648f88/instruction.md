# Bug Report

### Describe the bug

The `getEditUrl` function is not working correctly when `editUrl` is undefined or empty. It's now checking `fileRelativePath` instead of `editUrl` to determine whether to return a URL or undefined, which causes unexpected behavior.

### Reproduction

```js
import { getEditUrl } from '@docusaurus/utils';

// This should return undefined but returns a normalized URL instead
const result1 = getEditUrl('docs/intro.md', undefined);
console.log(result1); // Expected: undefined, Actual: normalized URL

// This should also return undefined but doesn't
const result2 = getEditUrl('docs/intro.md', '');
console.log(result2); // Expected: undefined, Actual: normalized URL

// Meanwhile, this incorrectly returns undefined
const result3 = getEditUrl('', 'https://github.com/user/repo/edit/main/');
console.log(result3); // Expected: URL, Actual: undefined
```

### Expected behavior

The function should return `undefined` when `editUrl` is falsy (undefined or empty string), regardless of whether `fileRelativePath` has a value. The edit URL should only be generated when a valid `editUrl` is provided.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
