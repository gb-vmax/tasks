# Bug Report

### Describe the bug

I'm encountering an issue with HTML rendering when using rehype-stringify. The output seems to be corrupted or malformed, and elements aren't being serialized correctly to HTML strings.

### Reproduction

```js
const rehype = require('rehype')
const html = require('rehype-stringify')

const tree = {
  type: 'element',
  tagName: 'div',
  properties: {},
  children: [
    {
      type: 'element',
      tagName: 'p',
      properties: {},
      children: [{type: 'text', value: 'Hello world'}]
    }
  ]
}

const result = rehype()
  .use(html)
  .stringify(tree)

console.log(result)
// Expected: <div><p>Hello world</p></div>
// Actual: Incorrect or malformed HTML output
```

### Expected behavior

The tree should be properly converted to valid HTML markup with all elements and their children correctly serialized.

### System Info

- rehype-stringify version: 10.0.0
- Node version: 18.x

---
Repository: /testbed
