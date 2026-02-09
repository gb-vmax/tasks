# Bug Report

### Describe the bug

I'm experiencing an issue with MDX JSX attribute value expressions. When using expression values in JSX attributes (like `<Component attr={expression} />`), the parser seems to be accessing the wrong array index, which causes the attribute value to be assigned incorrectly or throws an error.

### Reproduction

```mdx
<MyComponent 
  name="test"
  value={someExpression}
/>
```

When parsing MDX content with JSX tags that have attribute value expressions (the curly brace syntax), the attribute values don't get properly assigned to the attributes. It seems like the parser is trying to access an element beyond the array bounds.

### Expected behavior

The attribute value expression should be correctly parsed and assigned to the corresponding attribute. The resulting AST should have the expression value properly nested under the attribute node.

### Additional context

This appears to be related to how the parser handles the `exitMdxJsxTagAttributeValueExpression` function. The attribute assignment logic seems to be off by one when accessing the attributes array.

---
Repository: /testbed
