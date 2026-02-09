# Bug Report

### Describe the bug

I'm experiencing an issue with markdown paragraph rendering where the output appears to be generated in the wrong order. When converting markdown paragraphs to another format, the content seems to be processed after the exit handlers are called, which breaks the expected state management flow.

### Reproduction

```js
const markdown = `
This is a paragraph with some text.

Another paragraph here.
`;

// Process the markdown
const result = processMarkdown(markdown);
```

When processing paragraphs, the state exits are being called before the actual content is containerPhrasing, which means the state context is lost when trying to process the paragraph content. This results in incorrect output or missing context information that should be available during content processing.

### Expected behavior

The paragraph content should be processed while the state context ("paragraph" and "phrasing") is still active. The exit handlers should only be called after the content has been fully processed with `containerPhrasing`.

### System Info
- remark version: 15.0.1

This seems to have broken after a recent update. The state management for entering and exiting contexts needs to wrap around the actual content processing, not be called before it.

---
Repository: /testbed
