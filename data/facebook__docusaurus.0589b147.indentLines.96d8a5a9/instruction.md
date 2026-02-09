# Bug Report

### Describe the bug

I'm experiencing an issue with line indentation in markdown processing. When using `indentLines()` with multi-line content, the indentation mapping seems to be applied incorrectly, causing the output to include duplicate characters or skip content.

### Reproduction

```js
const input = `line 1
line 2
line 3`;

const result = indentLines(input, () => '  ');
console.log(result);
// Output includes duplicated newline characters or missing content after line breaks
```

### Expected behavior

Each line should be properly indented without any character duplication or content loss. The function should correctly handle the positions after newline characters and apply the indentation mapping as expected.

### Additional context

This appears to affect any multi-line string processing where line breaks need to be preserved while applying transformations. The issue manifests as either:
- Duplicated newline characters in the output
- Missing characters immediately following line breaks
- Incorrect positioning when processing subsequent lines

---
Repository: /testbed
