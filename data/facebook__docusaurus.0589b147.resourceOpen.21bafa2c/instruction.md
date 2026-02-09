# Bug Report

### Describe the bug
Markdown links with empty URLs are not being parsed correctly. When a link has no destination (e.g., `[text]()`), the parser seems to be handling it incorrectly.

### Reproduction
```markdown
[Click here]()
```

When parsing this markdown, the link is not processed as expected. The parser appears to be treating empty link destinations differently than it should.

### Expected behavior
Links with empty destinations should be parsed correctly. The parser should recognize `[text]()` as a valid (though empty) link structure.

### Additional context
This affects any markdown content that contains links with empty parentheses. The issue seems to be in how the resource tokenizer checks for the closing parenthesis.

---
Repository: /testbed
