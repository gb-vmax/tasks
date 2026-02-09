# Bug Report

### Describe the bug

I'm experiencing an issue with MDX JSX flow elements where the indentation is being applied incorrectly. When rendering nested JSX flow elements in MDX, the indentation logic seems to be inverted - blank lines are getting indented when they shouldn't be, and non-blank lines aren't getting the proper indentation.

### Reproduction

```mdx
<div>
  <p>Some content</p>
  
  <p>More content</p>
</div>
```

When this gets serialized, the indentation doesn't match what's expected. The JSX flow elements are either getting extra indentation when they shouldn't, or missing indentation entirely.

### Expected behavior

JSX flow elements should maintain proper indentation based on their nesting level. Non-blank lines should receive the current indent, while blank lines should remain unindented. The conditional logic should correctly identify which element types need indentation processing.

### Additional context

This appears to affect the serialization of MDX documents with nested JSX components. The indentation becomes inconsistent, making the output harder to read and potentially breaking some parsers that are sensitive to whitespace.

---
Repository: /testbed
