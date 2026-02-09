# Bug Report

### Describe the bug

I'm encountering an issue with MDX JSX tag parsing where self-closing tags in certain contexts are being incorrectly validated. The parser throws an error message about "Unexpected self-closing slash `/` in closing tag" even when the self-closing slash appears in a regular opening tag, not a closing tag.

### Reproduction

```mdx
<Component />
```

When parsing this valid self-closing JSX tag, the parser incorrectly throws an error claiming the self-closing slash is in a closing tag, when it's actually in a regular opening tag.

### Expected behavior

Self-closing tags like `<Component />` should be parsed without errors. The error message about unexpected self-closing slashes should only appear when there's actually a closing tag with a self-closing marker (like `</Component />`), which would indeed be invalid.

### Additional context

The error message itself is confusing because it says "Unexpected self-closing slash `/` in closing tag" but gets triggered in the wrong scenario. It seems like the validation logic for when to throw this error might be inverted.

---
Repository: /testbed
