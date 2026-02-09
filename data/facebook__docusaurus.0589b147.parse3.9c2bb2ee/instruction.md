# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where the tokenizer creation seems to be using incorrect parameters. When parsing MDX content with specific constructs, the parser doesn't properly handle the `from` context that's passed to the tokenizer creator.

### Reproduction

```js
const mdx = require('@mdx-js/mdx');

const content = `
# Hello

Some content here with **bold** text.

\`\`\`js
const x = 1;
\`\`\`
`;

const result = await mdx.compile(content, {
  // Custom parsing options
});
```

When compiling MDX with custom settings or constructs, the parser seems to lose track of the proper parsing context, causing unexpected behavior in how content is tokenized.

### Expected behavior

The tokenizer should correctly receive and use the `from` parameter to maintain proper parsing context throughout the document structure. Each tokenizer instance should be created with the appropriate context based on where it's being invoked from in the parsing tree.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node.js version: 18.x

---
Repository: /testbed
