# Bug Report

### Describe the bug

I'm encountering a parsing issue with variable declarations in MDX files. When declaring variables (using `var`, `let`, or `const`), the parser seems to be processing them in the wrong order, causing syntax errors or unexpected behavior.

### Reproduction

```mdx
export const myVariable = 'test';

# My Document

Some content here.
```

When trying to parse this MDX content, the variable declaration fails to parse correctly. The semicolon appears to be processed before the actual variable parsing happens, which breaks the expected syntax tree.

### Expected behavior

Variable declarations should be parsed in the correct order:
1. Parse the variable declaration
2. Process the semicolon
3. Finish the node

The parser should handle standard JavaScript variable declarations without errors.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This seems to have broken recently. Any MDX file with variable declarations at the top is affected.

---
Repository: /testbed
