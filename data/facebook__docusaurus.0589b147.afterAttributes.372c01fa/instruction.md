# Bug Report

### Describe the bug

I'm encountering an issue with directive parsing where leaf directives are causing unexpected behavior. After some recent changes, it seems like the whitespace handling after directive attributes is broken.

### Reproduction

```markdown
::directive[label]{attribute="value"}
```

When parsing this directive syntax, the parser appears to fail or produce incorrect results. The issue occurs specifically with leaf directives that have both labels and attributes.

### Expected behavior

The directive should be parsed correctly, with proper handling of whitespace after the attributes section. The parser should continue processing the rest of the content without errors.

### Additional context

This seems to affect any leaf directive that includes attributes. Text directives and container directives might be affected too but I haven't tested those extensively yet.

---
Repository: /testbed
