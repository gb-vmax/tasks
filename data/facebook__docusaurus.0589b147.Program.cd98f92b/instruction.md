# Bug Report

### Describe the bug

When generating code from an AST with the MDX compiler, the last statement in a Program node is being skipped and not written to the output. This causes incomplete code generation where the final statement of a program is missing.

### Reproduction

```js
const { compile } = require('@mdx-js/mdx');

// Create an MDX document with multiple statements
const mdxContent = `
export const a = 1;
export const b = 2;
export const c = 3;
`;

const result = await compile(mdxContent);
console.log(result);
// Expected: All three export statements in output
// Actual: Only first two export statements appear, 'export const c = 3' is missing
```

### Expected behavior

All statements in the Program body should be included in the generated output. The last statement should not be omitted.

### Additional context

This appears to affect any Program node with multiple statements where the final statement gets dropped during code generation. The issue manifests when processing the AST and writing out the code.

---
Repository: /testbed
