# Bug Report

### Describe the bug

I'm encountering an issue with MDX expression parsing where closing braces `}` are not being handled correctly. It seems like expressions are being closed prematurely or the parser is treating closing braces differently than expected.

### Reproduction

When using MDX expressions with braces, the parser appears to incorrectly process the closing brace. For example:

```mdx
{someExpression}
```

The closing brace `}` should only close the expression when the brace count is balanced (size === 0), but it seems like the condition for detecting the closing brace has changed.

### Expected behavior

The parser should only treat `}` as a closing brace when:
1. The character code is 125 (which is `}`)
2. AND the brace nesting level (size) is 0

Currently it appears that expressions might be closing at unexpected times, possibly when either condition is true rather than when both are true.

### System Info
- remark-mdx version: 3.0.0
- Node version: latest

---
Repository: /testbed
