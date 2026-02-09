# Bug Report

### Describe the bug

I'm experiencing an issue with JSX/MDX parsing where tags with certain attribute patterns are not being parsed correctly. It seems like the parser is incorrectly handling cases where attribute names contain specific characters or when there are null code points in the input stream.

### Reproduction

When parsing MDX content with JSX tags that have attributes, the parser fails to properly recognize the end of tag names in some edge cases:

```jsx
<Component attributeName="value" />
```

The issue appears when the code point is null or when certain character sequences are encountered during attribute parsing. The parser seems to be checking for null values incorrectly, which causes it to either skip valid attributes or fail to properly transition between parsing states.

### Expected behavior

The parser should correctly handle all valid JSX/MDX attribute syntax and properly transition between tag name parsing and attribute parsing states, regardless of the code point values encountered.

### Additional context

This seems related to how the parser validates code points when determining whether to exit tag name parsing. The condition for checking valid characters appears to have an issue with null handling that causes unexpected parsing behavior.

---
Repository: /testbed
