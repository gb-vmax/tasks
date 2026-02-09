# Bug Report

### Describe the bug

I'm encountering an issue with MDX parsing where content with nested structures is being processed incorrectly. It seems like there's an off-by-one error happening somewhere in the subcontent processing logic.

### Reproduction

When parsing MDX documents with nested content blocks (like lists within lists or nested components), the output is malformed. Here's a minimal example:

```mdx
<Container>
  <Item>First</Item>
  <Item>Second</Item>
  <Item>Third</Item>
</Container>
```

The parsed result has incorrect positioning/indexing, causing elements to be skipped or duplicated in the output.

### Expected behavior

Nested content should be parsed and rendered correctly with all elements appearing in the proper order and position.

### Additional context

This appears to be related to how the parser handles jumps and adjustments when processing child events. The issue manifests when there are multiple levels of nesting in the document structure.

---
Repository: /testbed
