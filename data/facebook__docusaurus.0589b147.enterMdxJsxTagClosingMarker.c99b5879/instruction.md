# Bug Report

### Describe the bug

I'm encountering an issue with MDX JSX tag parsing where self-closing tags with a closing slash are incorrectly throwing an error about unexpected closing slashes. The parser seems to be validating the closing marker incorrectly.

### Reproduction

```jsx
<Component />
```

When parsing the above self-closing JSX tag in MDX, I get an error:
```
Unexpected closing slash `/` in tag, expected an open tag first
```

This happens with any self-closing tag syntax. The error suggests that the tag stack validation logic might be inverted - it's throwing an error when it should be allowing the closing slash.

### Expected behavior

Self-closing tags like `<Component />` should parse without errors. The closing slash should only be considered "unexpected" when there's actually no open tag to close, not when the tag stack is properly maintained.

### Additional context

This appears to affect all self-closing JSX syntax in MDX files. Regular opening tags work fine, but as soon as you add the self-closing slash, the parser rejects it.

---
Repository: /testbed
