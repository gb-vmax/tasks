# Bug Report

### Namespace variable name gets overwritten on subsequent references

I'm encountering an issue where the name of a namespace variable changes unexpectedly when the same namespace is referenced multiple times with different identifiers.

### Reproduction

When a namespace is imported and then referenced multiple times (e.g., through different aliases or re-exports), the namespace variable's name property gets overwritten with each new reference instead of keeping the original name.

For example:
```js
import * as ns from './module';
export { ns };
export { ns as namespace };
```

In this case, the namespace variable's internal name keeps changing with each reference, which can lead to inconsistent behavior in the generated output.

### Expected behavior

The namespace variable should maintain its original name from the first reference, even when additional references are added. Subsequent references shouldn't modify the established name property.

### Additional context

This seems to affect scenarios where:
- A namespace is re-exported with different names
- Multiple identifiers refer to the same namespace import
- The namespace is aliased in various parts of the code

The name property appears to be getting reassigned every time `addReference` is called, rather than being set once and preserved.

---
Repository: /testbed
