# Bug Report

### Describe the bug

I'm experiencing an issue with text node handling in markdown processing. It appears that whitespace at the beginning and end of text nodes is being unexpectedly removed, which is breaking the formatting of my markdown output.

### Reproduction

When processing markdown with text nodes that have leading or trailing whitespace, the whitespace gets stripped:

```js
const node = {
  type: 'text',
  value: '  some text with spaces  '
}

// The output removes the leading/trailing spaces
// Expected: "  some text with spaces  "
// Actual: "some text with spaces"
```

This is particularly problematic when dealing with inline formatting where the spacing matters, like when you have text adjacent to emphasis or other inline elements.

### Expected behavior

Text nodes should preserve their original whitespace, including leading and trailing spaces. The markdown processor should output the text exactly as it appears in the value property without trimming.

### Additional context

This seems to have started happening recently. The whitespace preservation is important for maintaining proper spacing between inline elements in the rendered markdown.

---
Repository: /testbed
