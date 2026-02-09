# Bug Report

### Describe the bug

I'm encountering an issue where leading comments in my source files are being unexpectedly removed during the build process. Comments that appear at the very beginning of a file (before any code) are getting stripped out even though they should be preserved.

### Reproduction

Given a source file with leading comments:

```js
// This is an important header comment
// Copyright information here
/* Another comment block */

export function myFunction() {
  return 'hello';
}
```

After bundling, the output is missing the leading comments:

```js
export function myFunction() {
  return 'hello';
}
```

### Expected behavior

Leading comments (especially copyright notices, license headers, etc.) should be preserved in the output bundle. Previously these comments were kept intact at the top of the generated code.

### Additional context

This seems to have started happening recently. The comments are definitely present in the source files but don't make it to the final bundle. This is particularly problematic for license headers and copyright notices that need to remain in the distributed code.

---
Repository: /testbed
