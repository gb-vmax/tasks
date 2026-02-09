# Bug Report

### Describe the bug

When using `export default` declarations, the source code positioning is incorrect. The declaration start position is being calculated from the wrong location, which causes issues with code generation and source maps.

### Reproduction

```js
// Input file with export default
export default function myFunction() {
  return 'test';
}
```

When bundling this code, the output positioning is wrong. The declaration header isn't being properly identified - it's starting from the beginning of the export statement instead of after the "default" keyword.

### Expected behavior

The declaration start should be calculated by finding "default" in the export statement and then locating the first non-whitespace character after it (skipping the 7 characters in "default"). This ensures proper code positioning for transformations and source map generation.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
