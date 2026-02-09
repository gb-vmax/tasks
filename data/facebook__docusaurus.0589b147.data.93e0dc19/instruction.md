# Bug Report

### Describe the bug

I'm experiencing an issue with directive label parsing where backslash escapes aren't being handled correctly. When I try to escape special characters in directive labels using backslashes, the escaping doesn't work as expected.

### Reproduction

```markdown
:directive[Label with \[escaped brackets\]]

:directive[Text with backslash\\here]
```

When parsing these directives, the escaped characters are not being processed correctly. The backslash character seems to be treated differently than it should be.

### Expected behavior

Backslashes should properly escape special characters like brackets within directive labels. The parser should recognize `\[` and `\]` as escaped bracket characters and not treat them as label delimiters.

### Additional context

This appears to be related to how the parser handles escape sequences. The character code check for determining when to enter escape mode might not be correct - it seems like it's checking for the wrong character code.

---
Repository: /testbed
