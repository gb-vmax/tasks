# Bug Report

### Describe the bug

I'm encountering an issue with MDX JSX attribute value expressions where the wrong attribute is being assigned the expression value. When using expression values in JSX attributes, the value seems to be assigned to the incorrect attribute in the AST.

### Reproduction

```jsx
<Component 
  firstAttr="static"
  secondAttr={dynamicValue}
/>
```

When parsing the above MDX, the expression `{dynamicValue}` appears to be getting assigned to `firstAttr` instead of `secondAttr`. This causes the AST structure to be incorrect and breaks downstream processing.

### Expected behavior

The expression value should be correctly assigned to the attribute it's actually attached to (`secondAttr` in the example above), not to a different attribute in the list.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This appears to be a regression as it was working correctly in previous versions. Any help would be appreciated!

---
Repository: /testbed
