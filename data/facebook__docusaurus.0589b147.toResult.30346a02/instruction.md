# Bug Report

### Describe the bug

I'm experiencing an issue with the AST visitor utility where returning an array from a visitor function doesn't work as expected. The visitor seems to be wrapping the array in another array, which breaks the intended control flow.

### Reproduction

```js
import {visit} from 'unist-util-visit'

const tree = {
  type: 'root',
  children: [
    {type: 'paragraph', children: [{type: 'text', value: 'hello'}]},
    {type: 'paragraph', children: [{type: 'text', value: 'world'}]}
  ]
}

visit(tree, 'paragraph', (node, index) => {
  // Trying to return an array to control visit behavior
  return [SKIP, index + 1]
})
```

When I return an array from the visitor function (which should be treated as a tuple containing an action and an index), it seems like the array itself is being treated incorrectly. The expected behavior would be to use the array values directly to control the visiting logic, but instead it appears to be nested or handled improperly.

### Expected behavior

Returning an array like `[SKIP, 2]` from a visitor should be interpreted as a tuple where the first element is the action and the second is the index to continue from. The array should be used directly, not wrapped or modified.

### System Info
- unist-util-visit version: 5.0.0
- Node version: 18.x

---
Repository: /testbed
