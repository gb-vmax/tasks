# Bug Report

### Describe the bug

I'm encountering an issue with sourcemap generation where the first source file in the sourcemap is being skipped. When I build my project and examine the generated sourcemaps, the first entry in the `sources` array is not being processed correctly, which causes problems with debugging and source mapping.

### Reproduction

```js
// Build a project with multiple source files
// Check the generated sourcemap output
// The first source file is missing from the sourcemap processing

// Example sourcemap structure:
{
  sources: ['file1.js', 'file2.js', 'file3.js'],
  // ... other properties
}

// Expected: All three files should be processed
// Actual: Only file2.js and file3.js are being processed
```

### Expected behavior

All source files in the sourcemap should be processed, including the first one at index 0. The sourcemap should correctly map back to all original source files for proper debugging support.

### Additional context

This seems to affect the `ignorelist` functionality as well, since the first source file never gets its ignore list status checked. The loop appears to be starting at the wrong index.

---
Repository: /testbed
