# Bug Report

### Describe the bug

I'm encountering an issue with HTML text tokenization in the markdown parser. When processing inline HTML content, the parser seems to get stuck in an infinite loop or doesn't properly advance through the input.

### Reproduction

```js
const markdown = '<span>test</span>';
// Parser hangs or doesn't process correctly
const result = remark().parse(markdown);
```

When trying to parse simple inline HTML tags, the tokenizer appears to re-enter the `start` state repeatedly instead of progressing to the `open` state. This causes the parser to either hang indefinitely or fail to correctly tokenize the HTML content.

### Expected behavior

The parser should correctly tokenize inline HTML text by:
1. Entering the htmlText token
2. Entering the htmlTextData token
3. Consuming the opening `<` character
4. Transitioning to the `open` state to continue processing

Instead, it seems to be looping back to the start state.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
