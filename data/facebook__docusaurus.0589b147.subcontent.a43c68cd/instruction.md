# Bug Report

### Describe the bug

I'm encountering an issue with MDX parsing where content with line breaks is not being processed correctly. It seems like events are being skipped or indexed incorrectly when processing subcontent that spans multiple lines.

### Reproduction

```mdx
Some content here

Another paragraph with a break

More content
```

When parsing MDX content with void tokens that include line breaks, the event processing appears to be off by one. This causes some events to be skipped or incorrectly mapped, leading to malformed output or parsing errors.

### Expected behavior

The parser should correctly handle all events when processing subcontent with line breaks. Event indices should be properly tracked and no events should be skipped during the gap calculation phase.

### Additional context

This seems to affect content where:
- Void tokens span multiple lines
- There are enter/exit event pairs with line breaks between start and end positions

The issue appears to be in the subcontent event processing logic where break positions and gap adjustments are calculated.

---
Repository: /testbed
