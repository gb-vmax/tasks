# Bug Report

### Describe the bug

I'm experiencing an issue with MDX JSX attribute parsing where attribute names are being assigned to the wrong node in the attributes array. When parsing JSX tags with attributes, the attribute name gets applied to an incorrect element, causing the parsed AST to be malformed.

### Reproduction

```jsx
// Example MDX content with JSX attributes
<Component 
  firstAttr="value1"
  secondAttr="value2"
/>
```

When this is parsed, the attribute names don't get assigned to the correct attribute nodes in the AST. It seems like the parser is looking at the wrong index in the attributes array - specifically it's accessing `tag.attributes.length - 2` instead of the last attribute that was just added.

### Expected behavior

The parser should correctly assign attribute names to their corresponding attribute nodes. Each attribute should have its name properly set on the correct node in the attributes array (the most recently added one).

### Additional context

This appears to be related to how `exitMdxJsxTagAttributeNamePrimary` processes tokens. The function is accessing the wrong array index and also checking for the wrong node type (`mdxJsxExpressionAttribute` instead of `mdxJsxAttribute`), which causes attribute names to be misassigned during parsing.

---
Repository: /testbed
