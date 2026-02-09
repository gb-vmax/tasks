# Bug Report

### Describe the bug

I'm encountering an issue with attention sequence tokenization (like bold/italic markers) in MDX parsing. After a recent change, the parser seems to be calling `inside()` before properly entering the "attentionSequence" state, which causes the tokenization to fail or behave incorrectly.

### Reproduction

When parsing MDX content with emphasis markers:

```markdown
**bold text**
*italic text*
```

The attention sequences (asterisks) are not being tokenized correctly. The parser appears to be processing the marker character before the proper state is established.

### Expected behavior

The tokenizer should:
1. Enter the "attentionSequence" state
2. Then process the marker characters
3. Properly recognize bold/italic formatting

Instead, it seems like the order of operations got reversed, causing the sequence detection to break.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
