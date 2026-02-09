# Bug Report

### Describe the bug

I'm experiencing an issue with the MDX tokenizer where the state restoration is happening at the wrong time during construct handling. When a construct fails (`nok` is called), the parser state gets restored before trying the next construct in the list, but it seems like the restoration should only happen after all constructs have been exhausted.

### Reproduction

This is hard to reproduce with a minimal example, but the issue manifests when parsing MDX content with multiple possible constructs at a given position. The tokenizer tries constructs in sequence, and when one fails, it should preserve the state to try the next one. Currently, the state is being restored too early in the process.

The problematic behavior occurs in the `nok` callback within the `createTokenizer` function. When a construct doesn't match and we still have more constructs to try, the state restoration happens before incrementing the construct index, which can cause the parser to lose important context.

### Expected behavior

The tokenizer should only restore the parser state after all possible constructs have been tried and failed. During the iteration through the list of constructs, the state should be preserved so that each subsequent construct can be evaluated with the correct context.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
