# Bug Report

### Describe the bug

I'm experiencing an issue with fenced code blocks in MDX where the content parsing seems to be broken. After some recent changes, code blocks are not being processed correctly and the parser appears to be entering an incorrect state.

### Reproduction

```mdx
```javascript
const example = 'test';
console.log(example);
```
```

When parsing the above fenced code block, the tokenizer doesn't handle the content properly. The flow seems to skip over the actual code content or process it in the wrong order.

### Expected behavior

The fenced code block should be tokenized correctly with:
1. The opening fence being recognized
2. The code content being captured as `codeFlowValue`
3. The closing fence being processed
4. The entire block being properly parsed

Instead, it seems like the tokenizer is calling the wrong continuation function or skipping critical steps in the parsing flow.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This is affecting all fenced code blocks in my MDX documents. Any help would be appreciated!

---
Repository: /testbed
