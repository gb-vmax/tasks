# Bug Report

### Describe the bug

I'm encountering an issue with fenced code blocks in MDX where the closing fence sequence is not being recognized properly. When I try to use code blocks with backticks or tildes, the parser seems to fail at detecting where the code block should end.

### Reproduction

```mdx
```js
const example = 'test';
```
```

The code block doesn't close correctly and the content after it gets treated as part of the code block instead of regular markdown.

### Expected behavior

The parser should properly detect the closing fence sequence (matching backticks or tildes) and close the code block, allowing subsequent content to be parsed as normal markdown/MDX.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
