# Bug Report

### Describe the bug

Container directives are not being parsed correctly when they contain content. The directive content seems to be getting cut off or not recognized properly, causing the entire container to fail parsing.

### Reproduction

```markdown
:::note
This is some content inside a container directive.
It should be preserved as part of the directive.
:::
```

When parsing the above markdown with remark-directive, the content inside the container directive is not being processed correctly. The container appears to close prematurely or the content is not being captured.

### Expected behavior

The container directive should parse the entire content block between the opening `:::note` and closing `:::` markers. All content lines should be included in the directive's children nodes.

### Additional context

This seems to affect multi-line container directives specifically. Single-line directives appear to work fine. The issue appears when there's actual content between the opening and closing fence markers.

---
Repository: /testbed
