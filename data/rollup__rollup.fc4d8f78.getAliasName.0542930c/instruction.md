# Bug Report

### Describe the bug

The `getAliasName()` function is not correctly extracting the alias name from file paths. When passing a full file path, the function returns the entire path with the extension removed instead of just the base filename without extension.

### Reproduction

```js
import { getAliasName } from './utils/relativeId';

// Expected: 'myModule'
// Actual: '/some/path/to/myModule'
const aliasName = getAliasName('/some/path/to/myModule.js');
console.log(aliasName);

// Another example:
// Expected: 'index'
// Actual: 'src/components/index'
const aliasName2 = getAliasName('src/components/index.ts');
console.log(aliasName2);
```

### Expected behavior

The function should return only the base filename without the extension, not the full path. For example:
- `/some/path/to/myModule.js` should return `myModule`
- `src/components/index.ts` should return `index`

### System Info

- Version: latest
- Node: v18.x

---
Repository: /testbed
