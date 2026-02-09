# Bug Report

### Describe the bug

The `stripNumberPrefix` function is not working correctly - instead of removing the number prefix from strings, it's duplicating the content by appending the stripped filename to the original string.

### Reproduction

```js
import {stripNumberPrefix, stripPathNumberPrefixes} from '@docusaurus/plugin-content-docs';

// Example 1: Simple filename
const result1 = stripNumberPrefix('001-myDoc', stripPathNumberPrefixes);
console.log(result1);
// Expected: 'myDoc'
// Actual: '001-myDocmyDoc'

// Example 2: Folder path
const result2 = stripNumberPrefix('05-myFolder', stripPathNumberPrefixes);
console.log(result2);
// Expected: 'myFolder'
// Actual: '05-myFoldermyFolder'
```

### Expected behavior

The function should strip the number prefix and return only the filename/folder name without the prefix. Instead, it's concatenating the original string with the parsed filename, resulting in duplicated content.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This is breaking sidebar generation for docs with numbered prefixes.

---
Repository: /testbed
