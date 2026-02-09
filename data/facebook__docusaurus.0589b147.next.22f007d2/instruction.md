# Bug Report

### Describe the bug

I'm experiencing an issue with the MDX parser where the `lastTokEnd` property seems to be set at the wrong time during token parsing. This causes incorrect token position tracking when processing escape sequences in keywords.

### Reproduction

When parsing MDX content that contains keywords with escape sequences, the parser's internal state gets out of sync. The `lastTokEnd` value doesn't match the expected position because it's being updated before `nextToken()` is called instead of after.

This manifests when:
1. Parsing a keyword token
2. The keyword contains an escape sequence
3. The `next()` method is called with `ignoreEscapeSequenceInKeyword` parameter

The token end position gets recorded prematurely, leading to incorrect position information being available during the `nextToken()` call.

### Expected behavior

The `lastTokEnd` property should reflect the end position of the current token after `nextToken()` has been invoked, not before. This ensures that position tracking remains consistent throughout the parsing process.

### System Info
- @mdx-js/mdx version: 3.0.0
- Parser: acorn-based

---
Repository: /testbed
