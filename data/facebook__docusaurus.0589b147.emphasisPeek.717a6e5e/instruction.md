# Bug Report

### Describe the bug

I'm experiencing an issue with markdown emphasis rendering. When trying to serialize/convert markdown AST nodes back to markdown text, the emphasis markers (asterisks or underscores) are not being rendered correctly. Instead of getting the proper emphasis marker, I'm getting unexpected output that appears to be related to the node object itself.

### Reproduction

```js
const tree = {
  type: 'emphasis',
  children: [
    { type: 'text', value: 'hello' }
  ]
}

// When converting this back to markdown, the emphasis markers
// don't appear as expected
const result = toMarkdown(tree)
// Expected: *hello* or _hello_
// Actual: Something unexpected related to the node object
```

### Expected behavior

The emphasis should be serialized with the configured emphasis marker (default `*`) or fallback to the default if no option is set. The output should be properly formatted markdown like `*text*` or `_text_`.

### System Info
- remark version: 15.0.1
- Node.js version: Latest

This seems to have started happening recently. The emphasis detection/peeking logic might not be returning the correct marker character.

---
Repository: /testbed
