# Bug Report

### Describe the bug

I'm experiencing an issue with directive container parsing where closing fences are being accepted even when they have trailing content on the same line. According to the CommonMark spec for directives, a closing fence should only be valid if it's followed by optional whitespace and then a line ending (or end of file), but it seems like any content after the closing fence is now being accepted.

### Reproduction

```markdown
:::note
Some content here
::: trailing text that should invalidate the fence
```

The above should NOT close the container because there's text after the closing fence, but it appears to be treating it as a valid closing fence anyway.

Similarly:

```markdown
:::warning
Content
:::extra
```

This is also being parsed incorrectly - the `:::extra` should not be recognized as a valid closing fence since it has non-whitespace content after the colons.

### Expected behavior

A closing directive container fence should only be valid when:
1. It has the correct number of colons (at least as many as the opening fence)
2. It's followed by only whitespace
3. Then a line ending or EOF

Any trailing non-whitespace content on the same line as the closing fence should invalidate it, causing the parser to continue looking for a proper closing fence.

### Additional context

This seems to have changed recently and is affecting how nested directives and edge cases are being parsed. The parser should be stricter about what constitutes a valid closing fence.

---
Repository: /testbed
