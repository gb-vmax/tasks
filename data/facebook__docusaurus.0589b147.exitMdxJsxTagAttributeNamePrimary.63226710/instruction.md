# Bug Report

### Describe the bug

I'm experiencing an issue with MDX JSX attribute parsing where attribute names are being assigned to the wrong nodes. When parsing JSX tags with multiple attributes, the attribute name gets written to an incorrect position in the attributes array, causing the parser to fail or produce malformed output.

### Reproduction

```jsx
// MDX content with multiple attributes
<Component 
  firstAttribute="value1"
  secondAttribute="value2"
/>
```

When parsing this MDX content, the attribute names are not being correctly assigned to their corresponding attribute nodes. It appears that the parser is looking at the wrong index in the attributes array when setting the attribute name.

### Expected behavior

Each attribute name should be correctly assigned to its corresponding attribute node in the order they appear. The parser should handle multiple attributes on JSX tags without mixing up which name belongs to which attribute.

### System Info
- remark-mdx version: 3.0.0
- Node version: latest

---
Repository: /testbed
