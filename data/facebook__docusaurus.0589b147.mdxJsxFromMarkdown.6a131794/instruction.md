# Bug Report

### Describe the bug

I'm experiencing issues with JSX tag validation in MDX files. The parser is incorrectly accepting malformed closing tags that should be throwing errors, and it's also rejecting valid self-closing tags.

### Reproduction

```mdx
<Component>
  <NestedComponent />
</Component>
```

When parsing the above MDX content, the self-closing `<NestedComponent />` tag is being flagged as an error when it shouldn't be. The parser seems to think there's an issue with the closing slash.

Also, when I have mismatched tags like:

```mdx
<Outer>
  <Inner>
  </Inner>
</Outer>
```

The parser is not catching the mismatch correctly - it's throwing an error even when the tags are properly matched.

### Expected behavior

- Self-closing tags (e.g., `<Component />`) should be parsed without errors
- Properly matched opening and closing tags should be accepted
- Mismatched tags should throw appropriate validation errors

### Additional context

This seems to have started happening recently. The tag validation logic appears to be inverted or checking the wrong conditions. Both scenarios that should work and scenarios that should fail are behaving opposite to what's expected.

---
Repository: /testbed
