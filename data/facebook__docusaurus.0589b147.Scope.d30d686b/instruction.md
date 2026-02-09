# Bug Report

### Describe the bug

I'm experiencing issues with the MDX parser where variable declarations and scopes are getting mixed up between different parsing operations. When parsing multiple MDX files or parsing the same file multiple times, variables and functions declared in one file seem to leak into subsequent parses.

### Reproduction

```js
// Parse first MDX file
const result1 = await compile('export const foo = 1;');

// Parse second MDX file  
const result2 = await compile('export const bar = 2;');

// The second parse incorrectly "sees" declarations from the first parse
// Variables that should be scoped to each file are being shared
```

This also happens when:
1. Parsing the same MDX content multiple times in sequence
2. Running parallel parsing operations
3. Using the parser in a long-running process

### Expected behavior

Each parsing operation should have its own isolated scope. Variables, lexical declarations, and functions from one parse should not be visible or affect subsequent parses. The parser should maintain proper scope isolation between different invocations.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This is causing serious issues in our build pipeline where we process multiple MDX files, as declarations are bleeding across file boundaries.

---
Repository: /testbed
