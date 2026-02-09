# Bug Report

### Describe the bug

I'm experiencing an issue with directive parsing in remark. Text directives are no longer being recognized properly. When I try to use inline directives with the `:` syntax, they're not being parsed at all.

### Reproduction

```markdown
This is a :text-directive[with content] that should work.

Regular text here.
```

When processing this markdown with remark-directive, the text directive is not recognized and just appears as plain text in the output instead of being parsed as a directive node.

### Expected behavior

Text directives using the `:directive-name[content]` syntax should be properly tokenized and converted to directive nodes in the AST. They should be processed the same way they were in previous versions.

### Additional context

This seems to have started happening recently. Container and leaf directives with `::` and `:::` still work fine, but single-colon text directives are completely ignored now.

---
Repository: /testbed
