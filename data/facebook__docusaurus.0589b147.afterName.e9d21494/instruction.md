# Bug Report

### Describe the bug

I'm encountering an issue with inline directive parsing when using colons (`:`) in text directives. The parser seems to be rejecting directives that contain colons in unexpected ways, which is causing valid directive syntax to fail.

### Reproduction

```markdown
:directive-name:some text with content
```

When parsing the above markdown with remark-directive, the directive is not being recognized correctly. It appears that the presence of a colon after the directive name is causing the parser to reject it, even though this should be valid syntax for text directives.

### Expected behavior

Text directives with colons should be parsed correctly. The directive name should be extracted and the content following it should be processed as expected. The parser should handle the colon character appropriately based on its position in the directive syntax.

### Additional context

This seems to have started happening recently. I'm using text directives in my markdown content and they were working fine before, but now they're not being parsed at all. The issue specifically occurs when there's a colon character involved in the directive syntax.

---
Repository: /testbed
