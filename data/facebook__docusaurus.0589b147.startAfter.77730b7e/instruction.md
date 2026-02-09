# Bug Report

### Describe the bug

After a recent update, JSX/MDX tags with whitespace immediately after the opening `<` character are no longer being parsed correctly. Tags that have spaces or line breaks right after the opening bracket are now rejected, even though this should be valid syntax.

### Reproduction

```jsx
// This now fails to parse but should be valid:
< div>content</div>

// Also fails with newlines:
<
  div>content</div>

// Works fine (no whitespace after <):
<div>content</div>
```

### Expected behavior

Tags with whitespace (spaces, tabs, newlines) immediately after the opening `<` should be parsed successfully, as this is valid in JSX/MDX syntax. The parser should skip over the whitespace and continue processing the tag name.

### Additional context

This seems to have broken after a recent change to the tag parsing logic. The parser is now rejecting these patterns instead of handling the whitespace gracefully.

---
Repository: /testbed
