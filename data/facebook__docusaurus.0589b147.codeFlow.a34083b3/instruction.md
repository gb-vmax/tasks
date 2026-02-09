# Bug Report

### Describe the bug

After a recent update, code blocks in MDX files are not rendering correctly. The parser seems to be generating incorrect AST nodes for fenced code blocks, which causes them to either not display at all or display with broken formatting.

### Reproduction

```mdx
# My Document

Here's a code example:

```js
function hello() {
  console.log('world');
}
```

The code block above doesn't render properly.
```

When parsing this MDX content, the code block either disappears completely or renders as plain text instead of being properly formatted.

### Expected behavior

Code blocks should be parsed and rendered correctly with proper syntax highlighting and formatting, just like they were in previous versions.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
