# Bug Report

### Describe the bug

I'm experiencing an issue with import statement generation where the code crashes when processing import declarations with named imports. It seems like there's a problem with how the specifiers array is being iterated over.

### Reproduction

```js
// This causes an error when trying to generate code
const importNode = {
  type: 'ImportDeclaration',
  specifiers: [
    {
      type: 'ImportDefaultSpecifier',
      local: { name: 'foo' }
    },
    {
      type: 'ImportSpecifier',
      imported: { name: 'bar' },
      local: { name: 'bar' }
    }
  ],
  source: {
    type: 'Literal',
    value: './module'
  }
}

// When processing this node, it tries to access an undefined specifier
```

### Expected behavior

The import declaration should be correctly generated as:
```js
import foo, {bar} from './module';
```

Instead, the code attempts to access `specifiers[i]` where `i` is beyond the array bounds, resulting in `specifier` being `undefined` and causing a crash when trying to access `specifier.type`.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
