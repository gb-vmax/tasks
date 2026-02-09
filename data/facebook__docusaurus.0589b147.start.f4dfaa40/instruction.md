# Bug Report

### Describe the bug

I'm encountering an issue with markdown parsing where spaces at the beginning of lines are being handled incorrectly. It seems like the space tokenization logic has been changed and is now consuming characters before properly entering the token state, which causes unexpected behavior in the output.

### Reproduction

When parsing markdown content with leading spaces, the parser appears to process spaces in the wrong order. For example:

```markdown
  Some indented text
    More indented text
```

The spaces are being consumed before the token type is entered, and there's also a call to `markdownSpace()` being passed to the callback function which doesn't make sense in this context.

### Expected behavior

The parser should:
1. Enter the token type first
2. Then process/consume the space characters
3. Return the appropriate callback without wrapping it in additional function calls

The space handling should work consistently with how it was before, properly tracking the token state before consuming characters.

### System Info
- remark-gfm version: 4.0.0
- Parser: micromark-based

This appears to be a regression as the previous behavior was working correctly.

---
Repository: /testbed
