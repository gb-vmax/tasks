# Bug Report

### Describe the bug

I'm experiencing an issue with attention sequences (bold/italic markers like `*` and `_`) in MDX parsing. After a recent update, the tokenizer seems to be calling the `inside` function before entering the "attentionSequence" state, which causes the parsing to fail or behave incorrectly.

### Reproduction

```mdx
**bold text**
*italic text*
_underscored text_
```

When parsing MDX content with emphasis markers, the attention sequence tokenization doesn't work as expected. The parser appears to be processing the marker character before properly initializing the attention sequence state.

### Expected behavior

The parser should enter the "attentionSequence" state first, then begin processing the marker characters. Bold and italic text should be parsed correctly without errors.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
