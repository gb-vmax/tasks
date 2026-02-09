# Bug Report

### Describe the bug

I'm encountering an issue with keyword parsing where escape sequences in keywords are being reported incorrectly. It seems like the validation logic is inverted - escape sequences are being flagged when they shouldn't be, or not being flagged when they should be.

### Reproduction

```js
// When parsing code with escape sequences in keywords
// The error "Escape sequence in keyword" is raised at unexpected times

const code = `
  var x = 1;  // normal keyword
  var\u0020y = 2;  // keyword with escape sequence
`;

// The parser behavior seems inconsistent with when it should 
// raise the "Escape sequence in keyword" error
```

### Expected behavior

The parser should correctly identify and report escape sequences in keywords based on the `ignoreEscapeSequenceInKeyword` flag. When the flag is set to ignore them, no error should be raised. When it's not set to ignore them, the error should be raised appropriately.

Currently it seems like the logic is backwards - errors are being raised when they should be ignored and vice versa.

### Additional context

This appears to affect token parsing and may cause incorrect syntax error reporting during the parsing phase. The timing of when token state is updated might also be affecting how these errors are tracked.

---
Repository: /testbed
