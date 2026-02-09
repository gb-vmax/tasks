# Bug Report

### Describe the bug

The `normalizeUrl()` function is not properly handling URL normalization when combining protocol parts with paths. When passing a protocol and a single path component, the function fails to merge them correctly, resulting in malformed URLs.

### Reproduction

```js
import {normalizeUrl} from '@docusaurus/utils';

// This returns an incorrect URL
const result = normalizeUrl(['https:', 'example.com']);
console.log(result);
// Expected: 'https://example.com'
// Actual: 'https:example.com' (missing slashes)
```

Also seeing issues with trailing slash handling:

```js
const result2 = normalizeUrl(['https://example.com/', 'path/']);
console.log(result2);
// The trailing slash behavior seems inconsistent
```

### Expected behavior

- Protocol parts should be properly combined with the next component using the correct number of slashes
- Trailing slashes should be handled consistently for the last component in the URL array

### System Info
- @docusaurus/utils version: latest
- Node version: 18.x

This is breaking URL generation in my site config. Any help would be appreciated!

---
Repository: /testbed
