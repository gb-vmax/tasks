# Bug Report

### Describe the bug

I'm experiencing an issue with MDX code generation where the output is being unexpectedly cleared during compilation. When the same code fragment appears consecutively in the generated output, the entire output buffer gets reset instead of appending the code as expected.

### Reproduction

```js
// When compiling MDX content that generates duplicate consecutive code fragments
const mdxContent = `
# Hello
{someVariable}
{someVariable}
`;

// The compiled output loses previously generated code
// Expected: Full compiled output with both variables
// Actual: Output gets cleared when duplicate code is appended
```

This seems to happen when the code generation logic writes the same code string multiple times in succession. The output buffer is being cleared instead of accumulating the generated code.

### Expected behavior

The MDX compiler should accumulate all generated code in the output buffer, even when the same code fragment appears multiple times consecutively. Each `write()` call should append to the existing output, not clear it.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
