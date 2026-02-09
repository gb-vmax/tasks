# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where the compiler appears to be processing events beyond the array bounds. This is causing unexpected behavior when parsing certain markdown structures, particularly with lists and headings.

### Reproduction

When processing markdown with nested list items or complex heading structures, the parser seems to iterate one element too far in the events array. This can lead to:

1. Accessing undefined array elements
2. Incorrect spread detection in list items
3. Potential runtime errors when processing event handlers

Example markdown that triggers the issue:
```markdown
- First item
  - Nested item with blank line

  - Another nested item

# Heading with complex structure
```

The problem occurs during the compilation phase when iterating through events. The loop condition allows the index to equal the array length, which means it tries to access `events[events.length]` - an undefined element.

### Expected behavior

The compiler should only process valid events within the array bounds. List item spread detection should correctly identify blank lines without off-by-one errors, and event handlers should only be called for existing events.

### Additional context

This appears to affect:
- List item processing (spread detection logic)
- Event handler iteration
- General markdown compilation

The issue might not always throw an error but could cause subtle bugs in the generated AST or incorrect formatting of the output.

---
Repository: /testbed
