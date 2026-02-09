# Bug Report

### Describe the bug

I'm experiencing an issue where generated output from MDX compilation appears to be incomplete or truncated. When compiling MDX content, only the last chunk of code seems to be written to the output instead of accumulating all the generated code.

### Reproduction

```js
const {compile} = require('@mdx-js/mdx');

const mdxContent = `
# Hello World

This is a paragraph.

## Another heading

More content here.
`;

const result = await compile(mdxContent);
console.log(result.value);
// Output is incomplete - only contains the last generated chunk
```

### Expected behavior

The compiled output should contain the complete JavaScript code for the entire MDX document, with all sections properly included. Instead, it seems like earlier parts of the generated code are being overwritten rather than appended.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
