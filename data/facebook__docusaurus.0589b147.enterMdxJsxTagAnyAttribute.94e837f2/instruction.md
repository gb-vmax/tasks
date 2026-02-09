# Bug Report

### Describe the bug

When parsing MDX JSX tags, attributes are being incorrectly rejected on opening tags instead of closing tags. The validation logic appears to be inverted - it's throwing an error when attributes are added to opening tags (which should be allowed) rather than when they're added to closing tags (which should be disallowed).

### Reproduction

```jsx
// This should work but throws an error
<Component attribute="value">
  content
</Component>

// The error message says:
// "Unexpected attribute in closing tag, expected the end of the tag"
// But this is an opening tag, not a closing tag!
```

### Expected behavior

- Opening tags (`<Component attribute="value">`) should accept attributes without errors
- Closing tags (`</Component>`) should reject attributes and throw the error message
- The validation should correctly distinguish between opening and closing tags

### System Info
- @mdx-js/mdx version: 3.0.0

This seems like the condition check might be backwards? The error is being thrown in the wrong scenario.

---
Repository: /testbed
