# Bug Report

### Describe the bug

I'm experiencing an issue with JSX tag parsing in MDX files. When parsing JSX closing tags, the tokenization appears to be incorrect, which causes unexpected behavior in the resulting AST structure.

### Reproduction

```jsx
<Component>
  content here
</Component>
```

When parsing the closing tag `>` character, the marker tokens are being emitted in the wrong order. This results in an invalid token stream where:
1. A marker is entered
2. The marker is immediately exited (without consuming the character)
3. The character is consumed
4. The parent tag is exited
5. Another marker exit is emitted

This creates a malformed token structure that doesn't match the expected nesting.

### Expected behavior

The closing `>` character should be properly consumed within its marker token before exiting. The token stream should have proper enter/consume/exit ordering that maintains the correct nesting structure.

### Additional context

This seems to affect how the MDX parser handles the end markers of JSX tags. The issue is in the `tagEnd` function where the token effects are being called in an incorrect sequence.

---
Repository: /testbed
