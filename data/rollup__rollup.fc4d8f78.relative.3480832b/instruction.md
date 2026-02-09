# Bug Report

### Describe the bug

The `relative()` function in the path module is producing incorrect relative paths in certain cases. When computing the relative path between two directories, the function returns paths that don't correctly navigate from the source to the target.

### Reproduction

```js
import { relative } from './path'

// This returns an incorrect path
const result = relative('/a/b/c', '/a/b/d')
console.log(result) // Expected: '../d' but gets something else

// Another case that fails
const result2 = relative('/foo/bar', '/foo/baz/qux')
console.log(result2) // Expected: '../baz/qux'
```

When the two paths share a common prefix but then diverge, the relative path calculation doesn't work correctly. It seems like the logic for handling the path segments is broken.

### Expected behavior

The function should return a proper relative path that navigates from the `from` directory to the `to` directory using `..` to go up directories and then the remaining path segments.

For example:
- `relative('/a/b/c', '/a/b/d')` should return `'../d'`
- `relative('/a/b', '/a/c')` should return `'../c'`

### System Info
- Browser path module
- Affects path resolution logic

---
Repository: /testbed
