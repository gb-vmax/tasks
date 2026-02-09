# Bug Report

### Describe the bug

After a recent update, MDX files are failing to compile properly. The compilation process seems to get cut off mid-execution, resulting in incomplete JavaScript output. When trying to use MDX components, I'm getting syntax errors about unexpected end of input.

### Reproduction

```js
// Create a simple MDX file
const mdxContent = `
# Hello World

This is a test MDX file with some content.
`;

// Try to compile it
const result = await compile(mdxContent);
// Result is incomplete/truncated
```

The compiled output appears to be cut off partway through the function declaration, making the generated code invalid JavaScript.

### Expected behavior

MDX files should compile to complete, valid JavaScript code that can be executed without syntax errors. The entire function declaration and all necessary code should be present in the output.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
