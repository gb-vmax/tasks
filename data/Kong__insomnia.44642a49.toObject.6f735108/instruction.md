# Bug Report

### Describe the bug

I'm experiencing an issue with the `toObject()` method in the Variables class. After a recent update, calling `toObject()` on a Variables instance returns `undefined` instead of the expected merged object containing all variable scopes.

### Reproduction

```js
const variables = new Variables({
  globalVars: new Environment({ key1: 'global' }),
  collectionVars: new Environment({ key2: 'collection' }),
  environmentVars: new Environment({ key3: 'environment' }),
  iterationDataVars: new Environment({ key4: 'iteration' }),
  localVars: new Environment({ key5: 'local' })
});

const result = variables.toObject();
console.log(result); // Expected: { key1: 'global', key2: 'collection', ... }
                     // Actual: undefined
```

The method used to return a merged object with all variables from different scopes (global, collection, environment, iteration data, and local), but now it's returning undefined. This is breaking our variable resolution logic.

### Expected behavior

`toObject()` should return a merged object containing all variables from all scopes, with higher priority scopes overriding lower priority ones (local > iterationData > environment > collection > global).

### System Info
- insomnia-sdk version: latest
- Node.js version: 18.x

---
Repository: /testbed
