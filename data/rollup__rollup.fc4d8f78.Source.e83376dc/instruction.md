# Bug Report

### Describe the bug

I'm experiencing an issue with source map generation where the line and column numbers appear to be swapped in the final output. When I inspect the generated source maps, the mappings point to incorrect positions in the original source files.

### Reproduction

```js
// Original source file at line 10, column 5
function myFunction() {
  console.log('test');
}

// After bundling, the source map points to:
// line 5, column 10 instead of line 10, column 5
```

When debugging in browser dev tools, breakpoints and error stack traces show up at completely wrong locations in the source files. The line numbers seem to be where the column numbers should be and vice versa.

### Expected behavior

Source maps should correctly map the bundled code positions back to the original source file positions with accurate line and column numbers.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: macOS

---
Repository: /testbed
