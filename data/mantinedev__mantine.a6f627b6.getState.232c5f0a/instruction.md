# Bug Report

### Describe the bug

I'm experiencing a syntax error when trying to use the store from `@mantine/store`. The application fails to compile with a TypeScript error about the store interface definition.

### Reproduction

```ts
import { createStore } from '@mantine/store';

const store = createStore({ count: 0 });

// Attempting to use getState throws a compilation error
const currentState = store.getState();
```

The code fails to compile and I'm getting errors related to the store's type definition. It seems like there's something wrong with how the `MantineStore` interface is structured.

### Expected behavior

The store should be created successfully and `getState()` should return the current state value without any compilation errors.

### System Info
- @mantine/store version: latest
- TypeScript version: 5.x
- Node version: 18.x

---
Repository: /testbed
