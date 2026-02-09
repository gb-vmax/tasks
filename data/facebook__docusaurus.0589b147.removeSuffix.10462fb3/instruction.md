# Bug Report

### Describe the bug

The `removeSuffix` function is not removing suffixes correctly from strings. When I try to remove a suffix, it either returns an empty string when it shouldn't, or leaves part of the suffix still attached to the string.

### Reproduction

```js
import { removeSuffix } from '@docusaurus/utils';

// Case 1: Empty suffix returns empty string instead of original
const result1 = removeSuffix('hello', '');
console.log(result1); // Returns: '' 
// Expected: 'hello'

// Case 2: Valid suffix doesn't get fully removed
const result2 = removeSuffix('hello.txt', '.txt');
console.log(result2); // Returns: 'hello.t'
// Expected: 'hello'

// Case 3: Another example
const result3 = removeSuffix('index.md', '.md');
console.log(result3); // Returns: 'index.m'
// Expected: 'index'
```

### Expected behavior

- When suffix is an empty string, the original string should be returned unchanged
- When a valid suffix is provided, it should be completely removed from the end of the string

This is breaking my docs build where file extensions aren't being stripped properly.

---
Repository: /testbed
