# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where text content is not being recognized correctly. It seems like the parser is incorrectly identifying breaks in text content, causing normal text to be treated as something else.

### Reproduction

```mdx
This is a simple paragraph with some text.

Another paragraph here.
```

When parsing the above MDX content, the text is not being processed as expected. The parser appears to be misidentifying where text breaks occur, leading to incorrect parsing behavior.

### Expected behavior

The parser should correctly identify and process regular text content. Text that is not at a break point should be handled by the text construct, while actual breaks should be handled separately.

### Additional context

This seems to be related to the text initialization logic in the parser. The condition for determining whether content is at a break or is regular text appears to be inverted, causing the parser to make the wrong decision about how to process the content.

---
Repository: /testbed
