# Bug Report

### Describe the bug

I'm encountering an issue with HTML attribute rendering in rehype-stringify. When an attribute has a falsy value (like `false`, `null`, or `undefined`), the attribute name is being set as both the key and value instead of being omitted entirely.

### Reproduction

```js
const rehype = require('rehype');
const html = require('rehype-stringify');

const processor = rehype()
  .use(html);

const tree = {
  type: 'element',
  tagName: 'div',
  properties: {
    disabled: false,
    hidden: null,
    title: undefined
  },
  children: []
};

const result = processor.stringify(tree);
console.log(result);
// Expected: <div></div>
// Actual: <div disabled="disabled" hidden="hidden" title="title"></div>
```

### Expected behavior

Attributes with falsy values should be omitted from the output HTML. Only truthy values should render as attributes.

### System Info
- rehype-stringify version: 10.0.0
- Node version: 18.x

---
Repository: /testbed
