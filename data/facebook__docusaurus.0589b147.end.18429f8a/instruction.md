# Bug Report

### Describe the bug

I'm experiencing an issue with directive parsing in remark. When using directives with attributes, the parser seems to be failing to properly close the attributes section. The directive syntax isn't being recognized correctly and content that should be parsed as directives is being treated as regular text instead.

### Reproduction

```markdown
::directive{key="value"}
Content here
:::
```

When parsing this markdown, the directive attributes aren't being processed correctly. The closing brace `}` of the attributes should properly terminate the attributes section and allow the directive to be recognized, but instead the parser seems to reject the entire directive structure.

### Expected behavior

The directive should be properly parsed with its attributes recognized. The attributes section should close when encountering the `}` character, and the directive should be available in the AST for further processing.

### Additional context

This appears to affect all directives that use the attribute syntax with curly braces. Simple directives without attributes seem to work fine, but as soon as you add `{key="value"}` style attributes, the parsing breaks down.

---
Repository: /testbed
