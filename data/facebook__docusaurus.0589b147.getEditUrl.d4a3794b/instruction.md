# Bug Report

### Describe the bug

The `getEditUrl` function is returning `undefined` when an `editUrl` is provided, and attempting to generate a URL when `editUrl` is not provided. This is the opposite of the expected behavior.

### Reproduction

```js
import { getEditUrl } from '@docusaurus/utils';

// This returns undefined instead of a proper edit URL
const result1 = getEditUrl('docs/intro.md', 'https://github.com/user/repo/edit/main');
console.log(result1); // undefined (unexpected)

// This attempts to generate a URL with undefined editUrl
const result2 = getEditUrl('docs/intro.md', undefined);
console.log(result2); // Returns a malformed URL (unexpected)
```

### Expected behavior

When `editUrl` is provided, the function should return a normalized URL combining the edit URL and file path. When `editUrl` is not provided (undefined), it should return `undefined`.

```js
// Expected:
getEditUrl('docs/intro.md', 'https://github.com/user/repo/edit/main')
// Should return: 'https://github.com/user/repo/edit/main/docs/intro.md'

getEditUrl('docs/intro.md', undefined)
// Should return: undefined
```

### Additional context

This is breaking the "Edit this page" links in documentation sites. The links either don't appear when they should, or appear with malformed URLs when editUrl is not configured.

---
Repository: /testbed
