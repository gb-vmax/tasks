# Bug Report

### Describe the bug

When building with rollup and getting empty bundle warnings, the warning message displays incorrect information. The message shows "chunks" even when there's only a single empty chunk, and the wrong chunk name is displayed.

### Reproduction

```js
// Create a build that generates an empty bundle
// rollup.config.js
export default {
  input: 'src/empty.js',
  output: {
    file: 'dist/bundle.js'
  }
}

// src/empty.js (empty file or only exports that get tree-shaken)
export const unused = 'test';
```

Run the build and observe the warning message.

### Expected behavior

When a single empty chunk is generated:
- The message should say "Generated an empty chunk" (singular)
- The correct chunk name should be displayed

When multiple empty chunks are generated:
- The message should say "Generated empty chunks" (plural)
- All chunk names should be displayed correctly

### Actual behavior

The warning message incorrectly uses "chunks" for singular case and displays the wrong chunk name from the warnings array.

---
Repository: /testbed
