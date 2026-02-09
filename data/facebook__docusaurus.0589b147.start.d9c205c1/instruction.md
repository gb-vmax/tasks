# Bug Report

### Describe the bug

I'm encountering an issue with directive parsing after a recent update. When using directives with attributes, the parser seems to get stuck in an infinite loop or fails to properly parse the directive syntax.

### Reproduction

```markdown
::directive{#id .class key=value}
Content here
::
```

When processing markdown with directives that have attributes (using the `{...}` syntax), the parser doesn't advance correctly and appears to re-enter the start state instead of moving to the next parsing phase.

### Expected behavior

The directive attributes should be parsed correctly and the parser should move through the different states (start -> between -> attribute parsing) as expected. The directive should be recognized with its attributes and the content should be processed normally.

### System Info
- remark-directive version: 3.0.0
- Node version: Latest

This seems to have broken after some recent changes to the attribute factory function. The parser behavior has changed and directives with attributes are no longer working as they did before.

---
Repository: /testbed
