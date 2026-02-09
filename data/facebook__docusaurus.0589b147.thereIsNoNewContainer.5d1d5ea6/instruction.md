# Bug Report

### Describe the bug

I'm experiencing an issue with lazy line detection in markdown parsing. It appears that lines are being incorrectly marked as lazy when they shouldn't be, or vice versa. This affects how content is parsed within block containers like list items and block quotes.

### Reproduction

When parsing markdown with nested block structures, the lazy continuation logic seems inverted. For example:

```markdown
> quote line 1
continuation line
```

The continuation line's lazy status is being determined incorrectly, which affects how the parser handles the block structure.

### Expected behavior

Lines that are actual lazy continuations (lines that continue a block without the block marker) should be properly identified. The lazy flag should correctly reflect whether we stayed at the same container depth or entered/exited containers.

### Additional context

This seems related to how the parser tracks container depth when determining if a line is a lazy continuation. The logic for comparing the continued depth with the stack length might be inverted.

---
Repository: /testbed
