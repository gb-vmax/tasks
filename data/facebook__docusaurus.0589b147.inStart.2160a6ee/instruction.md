# Bug Report

### Describe the bug

I'm experiencing an issue with directive leaf syntax parsing in remark-directive. When trying to use the directive leaf syntax (single colon `:directive`), the parser is not recognizing valid directives correctly.

### Reproduction

```markdown
:myDirective[content]

:anotherDirective{key=value}
```

When parsing markdown with directive leaf syntax, the directives are not being processed. It seems like the parser is rejecting valid directive syntax at the start sequence level.

### Expected behavior

The directive leaf syntax should be properly recognized and parsed. Single colon directives like `:myDirective` should create the appropriate AST nodes with the directive name, content, and attributes.

### Additional context

This appears to have started happening recently. The directive container syntax (triple colon `:::`) and text directive syntax (double colon `::`) seem to work fine, but the leaf directive syntax is broken.

---
Repository: /testbed
