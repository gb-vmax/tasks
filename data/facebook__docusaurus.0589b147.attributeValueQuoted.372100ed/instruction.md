# Bug Report

### Describe the bug

I'm experiencing an infinite loop when parsing MDX files with quoted attribute values. The parser hangs and never completes when encountering JSX tags with attributes that have quoted values.

### Reproduction

```jsx
// This causes the parser to hang indefinitely
<Component attr="value" />

// Also happens with single quotes
<Component attr='value' />
```

The parser seems to get stuck in an infinite loop when processing the closing quote of attribute values. It never finishes parsing and the process has to be manually terminated.

### Expected behavior

The parser should successfully parse JSX tags with quoted attribute values and complete without hanging.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
