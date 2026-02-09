# Bug Report

### Describe the bug

The `stripNumberPrefix` function is returning an empty string when it should be returning the filename without the number prefix. After a recent change, files with number prefixes aren't being processed correctly and the function returns unexpected values.

### Reproduction

```js
import { stripNumberPrefix, DefaultNumberPrefixParser } from '@docusaurus/plugin-content-docs';

// This should return 'myDoc.md' but returns something else
const result = stripNumberPrefix('001-myDoc.md', DefaultNumberPrefixParser);
console.log(result); // Expected: 'myDoc.md', Actual: '[object Object]' or empty string
```

When processing files with number prefixes like `001-myDoc.md` or `02-myFolder`, the function no longer strips the prefix properly and returns incorrect values.

### Expected behavior

The function should return the filename with the number prefix removed:
- `001-myDoc.md` → `myDoc.md`
- `02-myFolder` → `myFolder`
- `5-test` → `test`

### System Info
- Docusaurus version: latest
- Node version: 18.x

This seems to have started happening recently and is breaking sidebar generation for numbered docs.

---
Repository: /testbed
