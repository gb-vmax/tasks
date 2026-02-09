# Bug Report

### Describe the bug

When bundling with `format: 'system'`, exported class declarations are being incorrectly processed. The system export statement is being appended when it shouldn't be, causing issues with the generated output.

### Reproduction

```js
// input.js
export class MyClass {
  constructor() {
    this.value = 42;
  }
}

// rollup.config.js
export default {
  input: 'input.js',
  output: {
    format: 'system',
    file: 'output.js'
  }
}
```

When bundling this code with the system format, the generated output includes an extra/incorrect system export statement for the class.

### Expected behavior

The class should be exported correctly in the system format without generating duplicate or incorrect export statements. The system export should only be added when the variable is actually in the `exportNamesByVariable` map.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
