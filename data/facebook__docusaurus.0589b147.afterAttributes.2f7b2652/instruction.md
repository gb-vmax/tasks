# Bug Report

### Describe the bug

I'm encountering an issue with directive container parsing where the whitespace handling after attributes seems broken. When I use directive containers with attributes, the parser appears to be stuck in an infinite loop or behaving unexpectedly.

### Reproduction

```markdown
:::note{#my-id .my-class}
Some content here
:::
```

When parsing the above directive container with attributes, the parser doesn't seem to properly advance after processing the attributes. It looks like the whitespace handling after the attribute block is not working as expected.

### Expected behavior

The directive container should parse correctly with attributes, properly handling any whitespace between the attributes and the content, and then continue parsing the rest of the document normally.

### System Info
- remark-directive version: 3.0.0

---
Repository: /testbed
