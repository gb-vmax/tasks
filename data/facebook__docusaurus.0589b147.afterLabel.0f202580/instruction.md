# Bug Report

### Describe the bug

I'm encountering an issue with directive container parsing where attributes are not being handled correctly. It appears that the condition for checking whether to attempt parsing attributes has been inverted - the parser is now attempting to parse attributes when it shouldn't, and skipping them when it should.

### Reproduction

```markdown
:::container[label]{#id .class}
content
:::
```

When parsing the above directive container syntax, the attributes `{#id .class}` are not being processed as expected. The parser seems to be checking for the wrong condition (checking `code !== 123` instead of `code === 123`) which causes it to attempt attribute parsing at the wrong time.

### Expected behavior

The parser should check if the current character code is `123` (which is `{`) before attempting to parse attributes. When a `{` is encountered after the label, it should parse the attributes inside the braces. Otherwise, it should skip attribute parsing and continue.

### Additional context

This affects any directive container that uses the attributes syntax with curly braces. The logic in `afterLabel` function appears to have the condition reversed, causing attributes to be parsed incorrectly or not at all.

---
Repository: /testbed
