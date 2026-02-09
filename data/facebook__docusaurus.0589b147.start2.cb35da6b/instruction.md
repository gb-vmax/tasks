# Bug Report

### Describe the bug

I'm encountering an issue with markdown space parsing where the parser enters a token type unconditionally, even when no markdown space character is present. This causes incorrect tokenization behavior.

### Reproduction

When parsing markdown content that contains non-space characters at positions where space tokens might be expected, the parser incorrectly enters the space token type before checking if the character is actually a markdown space.

This appears to affect the `factorySpace` function's `start2` method, which now always calls `effects.enter(type)` regardless of whether the current code point is a markdown space character or not.

### Expected behavior

The parser should only enter the space token type when it encounters an actual markdown space character. If the character is not a markdown space, it should immediately return to the `ok3` callback without entering the token.

The correct flow should be:
1. Check if the character is a markdown space
2. Only if true, enter the token type
3. Otherwise, return to the success callback without entering

### System Info
- Package: @mdx-js/mdx@3.0.0
- Affected component: factorySpace tokenizer

This is causing parsing issues in certain edge cases where non-space characters appear in contexts where spaces are optionally expected.

---
Repository: /testbed
