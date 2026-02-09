# Bug Report

### Describe the bug

I'm experiencing an issue with the markdown serialization where the output becomes corrupted when converting AST nodes back to markdown. The generated markdown contains duplicate content and the structure appears to be broken.

### Reproduction

```js
const tree = {
  type: 'root',
  children: [
    {
      type: 'paragraph',
      children: [
        { type: 'text', value: 'Hello world' }
      ]
    }
  ]
}

const markdown = toMarkdown(tree)
console.log(markdown)
// Expected: "Hello world\n"
// Actual: Corrupted output with duplicated/malformed content
```

When I try to convert an AST tree back to markdown, the resulting string doesn't match what I expect. It seems like something is going wrong with the internal state tracking during the serialization process.

### Expected behavior

The `toMarkdown` function should correctly serialize the AST tree back into valid markdown format without any corruption or duplication of content.

### System Info
- remark version: 15.0.1
- Node.js version: Latest

---
Repository: /testbed
