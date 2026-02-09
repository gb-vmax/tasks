# Bug Report

### Describe the bug

I'm experiencing an issue with directive parsing in remark-directive. When using text directives with colons, the parser seems to be incorrectly identifying or skipping certain character sequences. The behavior appears inconsistent - sometimes colons are properly recognized as part of directive syntax, and other times they seem to be treated differently than expected.

### Reproduction

```js
// Example directive with colon
:directive[text content]:

// Or nested cases
:outer[:inner[content]:]
```

The parser doesn't handle these cases correctly. It seems like the logic for checking previous characters or escape sequences might be off, causing directives with colons to either fail parsing or produce unexpected results.

### Expected behavior

Text directives should be parsed consistently regardless of colon placement. The parser should correctly identify when a colon is part of the directive syntax versus when it's escaped or part of the content.

### Additional context

This might be related to how the tokenizer checks for character escapes or validates directive boundaries. The issue manifests when processing markdown documents that contain multiple directives with colons in various positions.

---
Repository: /testbed
