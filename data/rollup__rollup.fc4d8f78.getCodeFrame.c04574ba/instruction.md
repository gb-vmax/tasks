# Bug Report

### Describe the bug
The code frame generation is showing incorrect line numbers. When an error occurs, the line numbers displayed in the error message are off by one - they're one less than the actual line where the error occurred.

### Reproduction
```js
// Given source code with an error on line 5
const source = `line 1
line 2
line 3
line 4
line 5 with error
line 6
line 7`;

const frame = getCodeFrame(source, 5, 10);
console.log(frame);
// Shows line 4 as the error line instead of line 5
```

### Expected behavior
The code frame should highlight the correct line number where the error actually occurred. If an error is on line 5, the frame should show line 5 as the error line, not line 4.

### System Info
- Version: latest
- Node: 18.x

---
Repository: /testbed
