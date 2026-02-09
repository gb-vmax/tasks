# Bug Report

### Describe the bug

The markdown parser appears to be hanging/freezing when processing setext-style headings (headings with underlines using `=` or `-` characters). The application becomes unresponsive and never completes parsing.

### Reproduction

```js
const markdown = `
My Heading
==========

Some content here
`;

// Parser hangs indefinitely when processing this
const result = remark().parse(markdown);
```

### Expected behavior

The parser should successfully parse setext-style headings and return the AST without hanging. The heading should be recognized and converted to the appropriate heading node.

### Additional context

This seems to affect both level 1 headings (underlined with `=`) and level 2 headings (underlined with `-`). Regular ATX-style headings (using `#` symbols) work fine, but setext headings cause the parser to get stuck in an infinite loop.

---
Repository: /testbed
