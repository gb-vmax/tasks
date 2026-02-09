# Bug Report

### Describe the bug

I'm experiencing an issue with MDX JSX attribute value expressions not being parsed correctly. When using expression values in JSX attributes within MDX files, the attribute values are being assigned to the wrong attribute or not being set at all.

### Reproduction

```mdx
<Component 
  name="test"
  value={someExpression}
/>
```

When parsing this MDX, the expression `{someExpression}` either:
1. Gets assigned to the wrong attribute (the one before it)
2. Doesn't get properly attached to the `value` attribute

This seems to affect any JSX tag in MDX that uses curly brace expressions for attribute values.

### Expected behavior

The expression value should be correctly assigned to the `value` attribute, not to `name` or any other preceding attribute. The parsed AST should have the attribute value expression attached to the correct attribute node.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
