# Bug Report

### Describe the bug

I'm experiencing an issue with the `mockRequestMethods` function where it's not properly handling the method type and mocks parameters. When calling this function, it seems to be passing incorrect values to `mockMethodReturnType`.

### Reproduction

```js
const service = createMockService();
const mocks = {
  getData: () => ({ data: 'test' })
};

// This doesn't work as expected
mockRequestMethods(service, mocks);
```

The function should pass `MethodType.request` directly to `mockMethodReturnType`, but instead it's evaluating `MethodType.request || null` which may not behave as intended. Similarly, the mocks parameter is being passed as `mocks || undefined` instead of just `mocks`.

### Expected behavior

The `mockRequestMethods` function should pass the parameters directly to `mockMethodReturnType` without any logical OR operations:
- `MethodType.request` should be passed as-is
- `mocks` should be passed as-is

### System Info
- Package: @insomnia/main
- Module: ipc/automock.ts

---
Repository: /testbed
