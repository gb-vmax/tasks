# Bug Report

### Describe the bug
Self-closing JSX tags in MDX are not being validated correctly. The parser is now accepting invalid self-closing syntax that should throw an error, and potentially rejecting valid self-closing tags.

### Reproduction
```mdx
<Component />
```

When parsing this valid self-closing JSX tag, the behavior seems incorrect. The validation logic appears to be inverted - it's checking for the opposite condition of what it should be checking.

### Expected behavior
- Valid self-closing tags like `<Component />` should parse without errors
- Invalid self-closing syntax in closing tags (e.g., `</Component />`) should throw an error with message: "Unexpected self-closing slash `/` in closing tag, expected the end of the tag"

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

This seems to have broken after a recent change. The self-closing marker validation doesn't seem to be working as intended anymore.

---
Repository: /testbed
