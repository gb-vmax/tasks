# Bug Report

### Describe the bug

The `docuHash` function is producing incorrect output for paths that start with `/`. It's returning `'index'` for any path beginning with a forward slash, not just the root path `'/'`.

Additionally, when the generated hash is too long and needs to be shortened, the kebab-case conversion is being applied in the wrong order, which results in malformed output.

### Reproduction

```js
import { docuHash } from '@docusaurus/utils';

// This incorrectly returns 'index' instead of a proper hash
console.log(docuHash('/docs'));
// Expected: something like 'docs-abc' 
// Actual: 'index'

console.log(docuHash('/api/reference'));
// Expected: something like 'api-reference-xyz'
// Actual: 'index'

// Only the root path should return 'index'
console.log(docuHash('/'));
// Expected: 'index'
// Actual: 'index' ✓ (this one works correctly)
```

For very long paths that exceed the filename length limit, the shortening logic also appears to be broken, producing garbled output instead of properly shortened kebab-case names.

### Expected behavior

- Only the exact path `'/'` should return `'index'`
- Other paths starting with `/` should be hashed normally
- Long paths should be shortened while maintaining proper kebab-case formatting

### System Info
- @docusaurus/utils version: latest
- Node version: 18.x

---
Repository: /testbed
