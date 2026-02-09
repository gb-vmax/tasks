# Bug Report

### Describe the bug

I'm experiencing an issue with remark-directive where directive names are not being parsed correctly. When I use directives in my markdown content, the directive name either doesn't get set properly or causes unexpected behavior.

### Reproduction

```markdown
::myDirective[content here]

:inlineDirective[text]

:::containerDirective
Some content
:::
```

When parsing the above markdown with remark-directive, the directive names don't seem to be extracted correctly. The resulting AST nodes either have incorrect or missing `name` properties.

### Expected behavior

The parser should correctly extract and assign the directive name (e.g., "myDirective", "inlineDirective", "containerDirective") to the corresponding AST node's `name` property.

### System Info
- remark-directive version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
