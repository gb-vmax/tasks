# Bug Report

### Describe the bug

I'm experiencing an issue with the `safeBound` function where it seems to be passing arguments in the wrong order. When using remark-stringify, certain markdown content is not being escaped properly, leading to incorrect output.

### Reproduction

```js
const remark = require('remark');
const stringify = require('remark-stringify');

const processor = remark().use(stringify);

const ast = {
  type: 'root',
  children: [
    {
      type: 'paragraph',
      children: [
        {
          type: 'text',
          value: 'Some text with special characters: * _ [ ]'
        }
      ]
    }
  ]
};

const result = processor.stringify(ast);
console.log(result);
// Expected: Special characters should be escaped correctly
// Actual: Characters are not escaped as expected
```

### Expected behavior

Special characters in markdown should be properly escaped based on the configuration context. The safe function should receive the correct arguments in the proper order (context, value, config).

### System Info
- remark version: 15.0.1
- Node version: 18.x

This seems to have broken after a recent update. The markdown output is now malformed in certain cases where character escaping is needed.

---
Repository: /testbed
