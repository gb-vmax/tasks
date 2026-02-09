# Bug Report

### Describe the bug

I'm experiencing an issue with JSX tag parsing in MDX content. When parsing JSX tags, the closing `>` character seems to be getting lost or not properly consumed, which causes the tag to not be recognized correctly.

### Reproduction

```jsx
// Simple JSX tag in MDX
<div>content</div>

// Self-closing tag
<Component />
```

When processing these tags, the closing angle bracket appears to not be included in the tag token, causing parsing issues downstream.

### Expected behavior

The closing `>` character should be properly consumed and included as part of the tag marker. The tag should be fully parsed with all its components (opening, attributes, and closing marker) correctly tokenized.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

This seems to have broken recently - tags were parsing fine before. The issue appears to affect both regular closing tags and self-closing tags.

---
Repository: /testbed
