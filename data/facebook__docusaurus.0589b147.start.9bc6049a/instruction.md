# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where whitespace handling seems broken. When parsing markdown content, the parser appears to be entering an infinite loop or behaving incorrectly when encountering spaces or whitespace characters.

### Reproduction

```js
const remark = require('remark');

const markdown = `
# Hello World

This is a test paragraph with spaces.
`;

const result = remark().parse(markdown);
// Parser hangs or produces incorrect output
```

### Expected behavior

The markdown parser should correctly handle whitespace and spaces in the content without hanging or producing malformed AST nodes. Spaces between words and around block elements should be processed normally.

### Additional context

This seems to affect any markdown content that contains spaces. The issue appears to be related to how the space factory function processes whitespace tokens. The parser either gets stuck or doesn't properly track the state when entering whitespace processing.

---
Repository: /testbed
