# Bug Report

### Describe the bug

I'm experiencing an issue with HTML entity encoding when using hexadecimal character references. It seems like the semicolon terminator is being incorrectly omitted in certain cases, which causes the output to be malformed.

### Reproduction

When converting characters to hexadecimal entities, the semicolon is not being added correctly. This happens when there's a following character that should require the semicolon to be present.

For example:
```js
// Converting a character followed by a hex digit
// Expected: &#x41;A
// Actual: &#x41A (semicolon missing, parsed as different entity)
```

The issue appears to be in the logic that determines whether to omit the semicolon. It's not properly checking if the next character could be ambiguous with the hex code.

### Expected behavior

Hexadecimal character references should always include the semicolon when the next character could be mistaken as part of the hex code (i.e., when it's a valid hex digit like 0-9, A-F, or a-f). Without the semicolon, `&#x41A` would be interpreted as U+041A (Cyrillic letter) instead of U+0041 followed by the letter 'A'.

### Additional context

This affects HTML output generation and could lead to incorrect character rendering in browsers, especially when entities are followed by hexadecimal characters.

---
Repository: /testbed
