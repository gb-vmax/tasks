# Bug Report

### Describe the bug

I'm encountering an issue with GFM table parsing where the parser seems to get stuck in an infinite loop when processing certain table structures. The browser tab becomes unresponsive and eventually crashes.

### Reproduction

```markdown
| Header |
| ------ |
| Cell 1 |
| Cell 2 |
```

When parsing the above markdown with GFM tables enabled, the parser enters an infinite loop during the tokenization phase. This happens specifically when the parser is checking for table continuation in the `start` function of the table tokenizer.

### Expected behavior

The table should parse correctly without hanging or crashing. The parser should properly identify table rows and move to the next parsing state.

### Additional context

This seems to happen when the loop condition for checking previous events doesn't properly terminate. The parser keeps iterating backwards through events indefinitely instead of stopping at the beginning of the events array.

---
Repository: /testbed
