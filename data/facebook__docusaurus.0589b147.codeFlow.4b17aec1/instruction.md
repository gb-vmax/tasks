# Bug Report

### Describe the bug

Code blocks in MDX files are not rendering correctly. Instead of being treated as code blocks, they seem to be processed as metadata nodes, which causes the content to either disappear or render incorrectly.

### Reproduction

```mdx
# Example Document

Some text before the code block.

```js
function hello() {
  console.log('world');
}
```

More text after.
```

When this MDX is processed, the code block doesn't render as expected. The JavaScript code either doesn't appear in the output or gets mangled somehow.

### Expected behavior

Code blocks should render properly with syntax highlighting and preserve their content. The example above should display the `hello` function in a formatted code block.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest LTS

---
Repository: /testbed
