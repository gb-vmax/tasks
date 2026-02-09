# Bug Report

### Describe the bug

The `addSuffix` function is not working as expected - it's adding the suffix to the beginning of the string instead of the end.

### Reproduction

```js
import { addSuffix } from '@docusaurus/utils';

const result = addSuffix('hello', 'world');
console.log(result); // Output: 'worldhello'
// Expected: 'helloworld'
```

When calling `addSuffix('hello', 'world')`, the function returns `'worldhello'` instead of `'helloworld'`. The suffix is being prepended rather than appended to the string.

### Expected behavior

The `addSuffix` function should append the suffix to the end of the string, not the beginning. For example:
- `addSuffix('test', '.md')` should return `'test.md'`
- `addSuffix('path/', '/')` should return `'path/'` (no duplicate)

### Additional context

This seems to have broken recently. The function is behaving more like a `addPrefix` function currently.

---
Repository: /testbed
