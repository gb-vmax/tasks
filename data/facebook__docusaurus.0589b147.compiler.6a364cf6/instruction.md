# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where line ending handling appears to be broken. When processing markdown content with certain structures, the parser seems to be using the wrong token type for checking if content can contain end-of-line characters.

### Reproduction

```js
const markdown = `
# Heading

Some text with
line breaks in
the middle
`;

const result = processor.parse(markdown);
// Line endings are not being handled correctly
```

### Expected behavior

Line endings should be properly processed based on the token type being evaluated. The parser should check whether the current token type (not the context type) can contain end-of-line characters before deciding how to handle line endings.

### Additional context

This seems to affect content that spans multiple lines within block-level elements. The parsing behavior changed recently and now line breaks within certain elements are not being preserved or handled as expected.

---
Repository: /testbed
