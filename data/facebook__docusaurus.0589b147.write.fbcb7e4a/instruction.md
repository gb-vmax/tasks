# Bug Report

### Describe the bug

I'm experiencing issues with the MDX compiler's code generation where output strings are being corrupted or replaced unexpectedly. The generated code appears to be missing content or getting truncated in certain scenarios.

### Reproduction

When compiling MDX content that contains specific patterns, the output code seems to get mangled. For example:

```js
// Input MDX with mixed content
const mdxContent = `
Some text here
<Component />
More text
`;

// After compilation, the generated output is incomplete
// Expected full output but getting truncated results
```

The issue seems related to how the compiler writes output internally. Content that should be appended is instead being replaced or cleared, particularly when there are newlines involved.

### Expected behavior

The compiler should correctly accumulate all generated code and produce complete output. All content should be properly appended without any truncation or replacement of previously written code.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This seems like a regression as earlier versions handled this correctly. Any help would be appreciated!

---
Repository: /testbed
