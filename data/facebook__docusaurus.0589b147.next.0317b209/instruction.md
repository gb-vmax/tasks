# Bug Report

### Describe the bug

I'm encountering an issue with the MDX parser where escape sequences in keywords are not being properly validated. It seems like the validation logic is inverted - escape sequences are being flagged when they shouldn't be, and vice versa.

### Reproduction

When parsing MDX content that contains keywords with escape sequences, the parser behavior is inconsistent:

```js
// This should raise an error but doesn't
const mdx = `export const my\u0056ar = 'test'`

// Meanwhile, normal keywords without escape sequences 
// are incorrectly flagged as having escape sequences
```

The `ignoreEscapeSequenceInKeyword` parameter appears to be having the opposite effect of what's intended.

### Expected behavior

The parser should raise a recoverable error when escape sequences are found in keywords (unless explicitly told to ignore them). Currently, it seems to do the opposite - only raising errors when the ignore flag is set to true.

### Additional context

This affects MDX parsing validation and could lead to invalid syntax being accepted or valid syntax being rejected. The timing of when token information is captured may also be affected, as there seems to be a change in when `nextToken()` is called relative to updating the last token position tracking.

---
Repository: /testbed
