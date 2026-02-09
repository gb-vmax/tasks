# Bug Report

### Describe the bug

I'm experiencing an issue with markdown heading formatting where headings are being rendered as setext-style (underlined with `===` or `---`) when they should be rendered as ATX-style (with `#` symbols), or vice versa.

The problem appears to be related to how the library detects line breaks within heading content. Headings that contain text nodes without line breaks are being incorrectly flagged as needing setext formatting.

### Reproduction

```js
const heading = {
  type: 'heading',
  depth: 2,
  children: [
    {
      type: 'text',
      value: 'Simple heading text'
    }
  ]
}

// This heading is being formatted incorrectly
// Expected: ## Simple heading text
// Actual: setext-style formatting is applied
```

### Expected behavior

Headings without actual line breaks (newline characters) or break nodes should be formatted as ATX-style by default. Only headings that actually contain line breaks in their text values or explicit break nodes should trigger setext formatting.

### Additional context

This seems to affect headings with regular text content. The detection logic for when to use setext vs ATX formatting appears to be inverted - it's treating normal text as if it contains line breaks.

---
Repository: /testbed
