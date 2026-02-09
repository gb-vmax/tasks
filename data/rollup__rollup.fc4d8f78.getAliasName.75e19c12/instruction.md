# Bug Report

### Describe the bug

The `getAliasName` function is returning incorrect results when extracting the base name from file paths. It appears to be cutting off the first character and sometimes returning empty strings when it should return the full filename without the extension.

### Reproduction

```js
import { getAliasName } from './utils/relativeId';

// Expected: 'myfile'
// Actual: '' (empty string)
console.log(getAliasName('myfile.js'));

// Expected: 'component'
// Actual: '' (empty string)
console.log(getAliasName('/path/to/component.vue'));

// Expected: 'index'
// Actual: '' (empty string)
console.log(getAliasName('index.ts'));
```

### Expected behavior

The function should return the filename without its extension. For example:
- `myfile.js` → `myfile`
- `component.vue` → `component`
- `index.ts` → `index`

Instead, it's returning empty strings or cutting off characters incorrectly.

### System Info
- Node version: 18.x
- OS: macOS

---
Repository: /testbed
