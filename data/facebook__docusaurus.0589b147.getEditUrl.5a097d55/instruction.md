# Bug Report

### Describe the bug

The `getEditUrl` function is returning `undefined` when a valid `editUrl` is provided, and attempting to normalize the URL when `editUrl` is `undefined` or empty. This is causing "Edit this page" links to not appear on documentation pages even when the edit URL is properly configured.

### Reproduction

```js
import {getEditUrl} from '@docusaurus/utils';

// This should return a valid edit URL but returns undefined
const result1 = getEditUrl('docs/intro.md', 'https://github.com/user/repo/edit/main');
console.log(result1); // Expected: 'https://github.com/user/repo/edit/main/docs/intro.md'
                      // Actual: undefined

// This should return undefined but tries to process the URL
const result2 = getEditUrl('docs/intro.md', undefined);
// This will likely throw an error or produce unexpected output
```

### Expected behavior

When `editUrl` is provided, the function should return the normalized URL combining the edit URL and file path. When `editUrl` is `undefined` or not provided, it should return `undefined`.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
