# Bug Report

### Describe the bug

I'm encountering an issue with markdown parsing where content is not being processed correctly. It seems like the parser is returning early or not completing the tokenization process properly.

### Reproduction

```js
const parser = remark();
const result = parser.parse('# Hello World\n\nSome content here');
```

When parsing markdown content, the parser appears to be cutting off or not returning the full set of events/tokens. The parsed output is incomplete or empty when it should contain the full document structure.

### Expected behavior

The parser should process the entire markdown input and return all tokenized events. All content should be captured and available in the parsed result.

### System Info
- remark version: 15.0.1
- Node version: Latest

This seems to have broken recently - parsing was working fine before. Not sure what changed but the tokenizer is definitely behaving differently now.

---
Repository: /testbed
