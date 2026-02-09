# Bug Report

### Describe the bug

Markdown link parsing is broken when there's whitespace after the URL in link syntax. Links that should be valid are not being recognized properly.

### Reproduction

```markdown
[link text](https://example.com )
```

The above markdown should parse as a valid link, but it's not being handled correctly. The whitespace after the URL but before the closing parenthesis seems to cause issues.

### Expected behavior

Links with trailing whitespace before the closing parenthesis should be parsed correctly, just like they are without the whitespace:

```markdown
[link text](https://example.com)  // works
[link text](https://example.com )  // should also work
```

This appears to have started happening recently. Not sure if this is related to recent changes in the markdown parser.

---
Repository: /testbed
