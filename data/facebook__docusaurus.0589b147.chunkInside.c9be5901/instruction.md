# Bug Report

### Describe the bug

I'm experiencing an infinite recursion issue when parsing certain MDX content. The parser seems to get stuck in an endless loop and eventually crashes with a stack overflow error.

### Reproduction

```js
// This causes the parser to hang indefinitely
const mdx = `
# Some content

Regular paragraph text
`;

const result = await compile(mdx);
```

When parsing MDX content that ends without a proper termination, the tokenizer enters an infinite loop instead of properly ending the content chunk.

### Expected behavior

The parser should gracefully handle the end of content and complete parsing without hanging or crashing. Content should be properly tokenized even when it reaches the end of the input.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to have started happening recently and is blocking our ability to parse any MDX files. The browser tab becomes unresponsive when trying to render the content.

---
Repository: /testbed
