# Bug Report

### Describe the bug

After a recent update, text nodes in MDX are being rendered incorrectly. It appears that empty text nodes are being converted to something else entirely, causing rendering issues in my components.

### Reproduction

When I try to render MDX content that contains text nodes, I'm getting unexpected behavior. For example:

```js
// Simple MDX content with text
const content = `
Hello world

This is a paragraph
`

// After processing, text nodes seem to have wrong type/value
// Expected: { type: "text", value: "" }
// Getting: something different that breaks rendering
```

The issue seems to affect empty text nodes specifically. Instead of being rendered as text elements with empty strings, they're being transformed into something else.

### Expected behavior

Text nodes should maintain their `type: "text"` and have a string value (even if empty). The current behavior breaks text rendering in MDX documents.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This is causing problems in production where MDX content isn't rendering properly. Any text that should be displayed is either missing or showing up as the wrong element type.

---
Repository: /testbed
