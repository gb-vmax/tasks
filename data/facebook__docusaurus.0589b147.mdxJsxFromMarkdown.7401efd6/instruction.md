# Bug Report

### Describe the bug

I'm encountering an issue with MDX JSX tag parsing where closing tags are not being validated correctly. It seems like mismatched opening and closing tags are not throwing errors when they should, and valid matching tags are throwing errors incorrectly.

### Reproduction

```jsx
// This should throw an error but doesn't:
<Component>
  <NestedComponent>
  </Component>
</NestedComponent>

// This should work but throws an error:
<Component>
  content
</Component>
```

When parsing MDX content with nested JSX tags, the parser is behaving unexpectedly - it's allowing mismatched tags to pass through without errors, while simultaneously rejecting properly matched tags with error messages about unexpected closing tags.

### Expected behavior

The parser should:
1. Accept properly matched opening and closing tags without errors
2. Throw an error when a closing tag doesn't match its corresponding opening tag
3. Properly track the tag stack to validate nesting

### System Info
- remark-mdx version: 3.0.0

---
Repository: /testbed
