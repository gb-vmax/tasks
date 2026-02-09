# Bug Report

### Describe the bug

I'm experiencing an issue with MDX tag parsing where certain valid JSX tags are not being recognized properly. It seems like the parser is incorrectly handling some edge cases when determining if a character can start an attribute name after a tag name.

### Reproduction

```jsx
// This should parse correctly but doesn't
<Component>content</Component>

// The issue appears when the parser encounters specific character codes
// after the tag name and tries to determine if it's valid
```

When rendering MDX content with certain JSX components, the parser crashes or fails to properly identify the end of tag names, particularly when checking for valid attribute start characters.

### Expected behavior

The parser should correctly identify when a tag name ends and attributes or tag closure begins. All valid JSX syntax should be parsed without errors.

### Additional context

This seems related to how the parser validates character codes after consuming a tag name. The logic for determining whether a character is valid in the context of "after name" appears to have an issue with the conditional check.

---
Repository: /testbed
