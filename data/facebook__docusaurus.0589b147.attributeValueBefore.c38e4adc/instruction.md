# Bug Report

### Describe the bug

I'm encountering an issue with MDX attribute parsing where quoted attribute values seem to break when using certain special characters. The parser appears to be handling the quote markers incorrectly, causing the attribute value to not be recognized properly.

### Reproduction

```mdx
<Component prop="value with quotes" />
```

When I try to use a component with a quoted attribute value like above, the attribute doesn't seem to be parsed correctly. The issue appears to be related to how the parser handles the opening quote marker.

### Expected behavior

Quoted attribute values should be parsed correctly and the component should receive the proper prop value. The parser should handle both single and double quotes as valid attribute value delimiters.

### Additional context

This seems to affect any component with quoted attribute values. I noticed this started happening recently but I'm not sure what changed. The MDX content renders but the attributes don't seem to be passed through correctly to the component.

---
Repository: /testbed
