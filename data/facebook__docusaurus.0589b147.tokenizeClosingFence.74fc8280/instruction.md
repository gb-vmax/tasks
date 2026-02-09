# Bug Report

### Describe the bug

I'm experiencing an issue with directive container parsing in remark-directive where closing fences with the same number of colons as the opening fence are not being recognized properly. The parser seems to reject valid closing fences that should match the opening sequence.

### Reproduction

```markdown
::: note
Content here
:::
```

When parsing this directive container, the closing fence `:::` (3 colons) should properly close the opening fence `:::` (also 3 colons), but it appears the parser is not accepting it as a valid closing sequence.

The issue seems to occur specifically when the closing fence has exactly the same number of colons as the opening fence. Closing fences with more colons than the opening work fine, but equal-length sequences fail.

### Expected behavior

A closing fence should be valid when it has the same number of colons OR more colons than the opening fence. Currently it only works with MORE colons, which breaks standard directive container syntax.

Example that should work but doesn't:
```markdown
::: container
text
:::
```

Example that works (but shouldn't be required):
```markdown
::: container  
text
::::
```

This is affecting basic directive container functionality and making it impossible to use standard syntax patterns.

---
Repository: /testbed
