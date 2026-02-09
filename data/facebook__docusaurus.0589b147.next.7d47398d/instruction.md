# Bug Report

### Describe the bug

I'm experiencing an issue with keyword parsing where escape sequences in keywords are not being properly validated. The parser appears to be raising errors for escape sequences even when `this.type.keyword` is undefined or null.

### Reproduction

```js
// Parser encounters a token with an escape sequence but no keyword type
// Example: parsing "\u0069dentifier" where containsEsc is true but type.keyword is undefined

const parser = new Parser(options, input, startPos);
parser.next(false); // Should only raise error if token is actually a keyword
```

### Expected behavior

The parser should only raise an error about escape sequences when the token is actually a keyword. If `this.type.keyword` is falsy (undefined/null), no error should be raised even if `containsEsc` is true.

Currently it seems like the validation logic is incorrectly structured, causing false positives when processing tokens with escape sequences that aren't keywords.

### Additional context

This affects parsing of identifiers and other non-keyword tokens that may contain valid escape sequences. The error message "Escape sequence in keyword undefined" suggests the condition is being evaluated incorrectly.

---
Repository: /testbed
