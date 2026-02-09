# Bug Report

### Describe the bug

I'm encountering an issue with HTML entity encoding in text nodes. When rendering text content inside elements, the wrong characters are being escaped/encoded. Specifically, it seems like `>` characters are being encoded when they shouldn't be, and `<` characters are not being encoded when they should be.

### Reproduction

```js
const tree = {
  type: 'element',
  tagName: 'div',
  children: [
    {
      type: 'text',
      value: 'Hello <world>'
    }
  ]
}

// Expected output: Hello &lt;world>
// Actual output: Hello <world> (or incorrect encoding)
```

When text contains `<` characters, they should be encoded as `&lt;` to prevent them from being interpreted as HTML tags. However, the output doesn't seem to be escaping these characters properly.

### Expected behavior

Text content containing `<` and `&` should be properly encoded as HTML entities (`&lt;` and `&amp;` respectively) to ensure they display correctly and don't break the HTML structure.

### Additional context

This appears to affect regular text nodes but not `<script>` or `<style>` tags (which is correct - those should preserve their raw content).

---
Repository: /testbed
