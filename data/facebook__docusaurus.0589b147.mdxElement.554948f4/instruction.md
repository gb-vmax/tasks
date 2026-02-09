# Bug Report

### Describe the bug

I'm experiencing an issue with MDX JSX serialization where the code appears to be truncated mid-function. When processing MDX JSX elements with attributes, the serialization logic seems incomplete and cuts off unexpectedly during the attribute formatting section.

### Reproduction

```js
const mdxContent = `
<Component
  prop1="value1"
  prop2="value2"
  prop3="value3"
/>
`;

// Process MDX content with attributes on their own lines
// The serialization fails or produces incomplete output
```

### Expected behavior

The MDX JSX elements should be properly serialized with all attributes formatted correctly, whether they're on one line or multiple lines. The function should complete the serialization logic for both inline and multi-line attribute layouts.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

The issue seems to occur specifically when handling attributes that need to be placed on their own lines due to line length constraints or line breaks in expressions.

---
Repository: /testbed
