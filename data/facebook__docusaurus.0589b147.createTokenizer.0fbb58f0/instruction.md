# Bug Report

### Describe the bug

I'm experiencing an issue with the tokenizer where constructs are being processed in the wrong order. It seems like the tokenizer is now iterating through the list of constructs backwards instead of forwards, which causes parsing to fail or produce unexpected results.

### Reproduction

When parsing content with multiple construct handlers, the last construct in the list is now being tried first instead of the first construct. This breaks the expected precedence order for tokenization.

Example scenario:
1. Register multiple constructs for handling different syntax patterns
2. The constructs should be tried in order from first to last
3. Instead, they're being tried from last to first

This causes constructs that should have lower priority to be matched before higher priority ones, leading to incorrect parsing behavior.

### Expected behavior

Constructs should be processed in the order they appear in the list (first to last), not in reverse order. The tokenizer should try the first construct, and if it fails, move to the next one sequentially.

### Additional context

This appears to have started happening recently. The iteration logic seems to have been changed, causing the construct index to start at the end of the list rather than the beginning.

---
Repository: /testbed
