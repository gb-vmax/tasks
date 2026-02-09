# Bug Report

### Describe the bug

I'm experiencing an issue with markdown generation where the output is missing proper newline characters at the end. It seems like the logic for appending a final newline is broken - sometimes it adds a newline when it shouldn't, and other times it doesn't add one when it should.

### Reproduction

```js
const tree = {
  type: 'root',
  children: [
    {
      type: 'paragraph',
      children: [{ type: 'text', value: 'Hello world' }]
    }
  ]
}

const result = toMarkdown(tree)
// Expected: "Hello world\n"
// Getting inconsistent results depending on the last character
```

Also noticing that when converting AST nodes to markdown, the state stack seems to behave strangely - elements are being popped immediately after being pushed, which causes context issues during traversal.

### Expected behavior

The markdown output should always end with a proper newline character when appropriate. The state stack should maintain the correct nesting context throughout the conversion process.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
