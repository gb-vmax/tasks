# Bug Report

### Describe the bug

I'm encountering an issue with footnote definition parsing in GFM (GitHub Flavored Markdown). When a footnote definition has an empty label (just `[^]:`), it's being accepted when it should be rejected. Additionally, duplicate footnote definitions are now being rejected incorrectly.

### Reproduction

```markdown
[^]: This should not be valid

[^note]: First definition
[^note]: Duplicate definition - this should be allowed but is being rejected
```

The first case with an empty label `[^]:` is incorrectly parsed as valid, when it should fail because there's no actual identifier between the brackets.

The second case with duplicate footnote identifiers is now being rejected when both definitions should be processed (typically the first one is used and subsequent ones are ignored, but they shouldn't cause parsing to fail).

### Expected behavior

1. Footnote definitions with empty labels (no identifier) should be rejected during parsing
2. Duplicate footnote definitions should be allowed to parse successfully (even if only the first one is used)

### System Info
- remark-gfm version: 4.0.0
- Parser: micromark-based

---
Repository: /testbed
