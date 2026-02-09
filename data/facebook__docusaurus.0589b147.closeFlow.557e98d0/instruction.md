# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where documents aren't being properly finalized. It seems like the flow isn't being closed correctly, which causes the parser to hang or produce incomplete output.

### Reproduction

```js
const processor = remark();
const result = processor.processSync('# Heading\n\nParagraph text');
// Parser appears to hang or produces incomplete AST
```

When processing markdown documents, especially those with multiple blocks (headings, paragraphs, lists, etc.), the parser doesn't complete properly. The document flow seems to remain open even after all content has been processed.

### Expected behavior

The markdown processor should properly close all flows and finalize the document, producing a complete AST without hanging.

### System Info
- remark version: 15.0.1
- Node version: Latest LTS

---
Repository: /testbed
