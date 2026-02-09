# Bug Report

### Describe the bug

I'm experiencing an issue with the markdown serialization where special characters that need escaping are not being handled in the correct order. When I have multiple special characters in my markdown content, they seem to be escaped in an inconsistent sequence, which leads to malformed output.

### Reproduction

```js
const markdown = remark()
  .use(remarkStringify)
  .stringify({
    type: 'root',
    children: [
      {
        type: 'paragraph',
        children: [
          { type: 'text', value: 'Text with * and # and _' }
        ]
      }
    ]
  })

console.log(markdown)
// Expected: Characters escaped in a predictable order
// Actual: Escaping order appears reversed or inconsistent
```

### Expected behavior

Special characters should be escaped in a consistent, predictable order (e.g., ascending order based on character code). This ensures that the output is deterministic and matches expected patterns.

### System Info
- remark version: 15.0.1
- Node version: 18.x

The ordering seems to have changed recently and is causing issues with our markdown generation pipeline where we rely on consistent output formatting.

---
Repository: /testbed
