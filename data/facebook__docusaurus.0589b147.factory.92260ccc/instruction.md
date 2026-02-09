# Bug Report

### Describe the bug

I'm experiencing an issue where the vendored `unist-util-remove-position` module appears to be corrupted or incomplete. When trying to use position removal functionality on AST nodes, the code fails unexpectedly.

### Reproduction

```js
const {removePosition} = require('./jest/vendor/unist-util-remove-position@5.0.0.js');

const tree = {
  type: 'root',
  children: [
    {
      type: 'paragraph',
      position: {
        start: {line: 1, column: 1},
        end: {line: 1, column: 10}
      },
      children: []
    }
  ],
  position: {
    start: {line: 1, column: 1},
    end: {line: 1, column: 10}
  }
};

// This should remove position info but throws an error
removePosition(tree);
```

### Expected behavior

The function should successfully traverse the tree and remove all position information from the nodes without throwing any errors.

### Additional context

Looking at the vendored file, it seems like the `factory` function definition might be truncated or malformed. The code appears to cut off mid-statement which would definitely cause parsing issues.

---
Repository: /testbed
