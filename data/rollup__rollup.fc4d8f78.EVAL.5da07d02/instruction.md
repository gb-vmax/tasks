# Bug Report

### Describe the bug

When EVAL warnings are displayed, the warning message appears incorrectly. Instead of showing the proper warning title "Use of eval is strongly discouraged", the URL is being displayed as the title.

### Reproduction

Trigger an EVAL warning in Rollup by using `eval` in your code:

```js
// example code that triggers EVAL warning
const result = eval('2 + 2');
```

When the warning is batched and displayed, you'll see the URL printed where the title should be, and the informational URL appears twice in the output.

### Expected behavior

The warning should display:
1. Title: "Use of eval is strongly discouraged"
2. Info URL: Link to the documentation about avoiding eval
3. Truncated warnings list

Instead, it currently shows the URL as the title.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
