# Bug Report

### Describe the bug

I'm experiencing an issue with markdown emphasis/strong parsing where the opening and closing logic seems broken. When using asterisks or underscores for emphasis, the parser is not correctly identifying which sequences should open and which should close emphasis spans.

### Reproduction

```js
// Example cases that are failing:
const text1 = "*foo* bar";  // Should parse correctly but doesn't
const text2 = "**strong text**";  // Strong emphasis not working as expected
const text3 = "_emphasis_";  // Underscore emphasis behaving incorrectly
```

The issue appears to be related to how the parser classifies characters before and after the attention markers. It seems like the logic for determining whether a sequence opens or closes emphasis is using the wrong character classification.

### Expected behavior

The parser should correctly identify:
- Opening emphasis markers (e.g., the first `*` in `*foo*`)
- Closing emphasis markers (e.g., the second `*` in `*foo*`)
- Whether emphasis can open/close based on surrounding whitespace and punctuation

Right now it's treating both the before and after characters the same way, which breaks the open/close detection logic.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
