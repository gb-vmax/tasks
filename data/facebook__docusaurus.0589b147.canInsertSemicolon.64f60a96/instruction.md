# Bug Report

### Describe the bug

I'm encountering an issue with automatic semicolon insertion (ASI) in MDX parsing. It seems like semicolons are not being inserted correctly in certain edge cases, particularly when dealing with closing braces.

### Reproduction

When parsing MDX content with JavaScript expressions that should trigger automatic semicolon insertion, the parser fails to insert semicolons where they should be according to ASI rules.

Example that triggers the issue:
```jsx
{
  const x = 1
}
{
  const y = 2
}
```

The parser seems to incorrectly determine when it's safe to insert a semicolon, especially around closing braces and line breaks.

### Expected behavior

The parser should correctly identify positions where automatic semicolon insertion should occur based on:
1. End of file
2. Closing braces with proper line break detection
3. Line breaks between statements

The current behavior appears to have the logic reversed or incorrectly checking for line breaks in the wrong position.

### System Info
- remark-mdx version: 3.0.0

---
Repository: /testbed
