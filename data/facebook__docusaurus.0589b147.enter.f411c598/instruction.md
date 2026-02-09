# Bug Report

### Describe the bug

I'm experiencing an issue with markdown serialization where the output seems to have corrupted structure. When converting AST nodes back to markdown, the generated output appears malformed and the conversion process crashes or hangs.

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
// Process hangs or produces unexpected output
```

### Expected behavior

The `toMarkdown` function should properly convert the AST tree back to valid markdown text without hanging or producing malformed output. The internal state tracking should work correctly during the serialization process.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
