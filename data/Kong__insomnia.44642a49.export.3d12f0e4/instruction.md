# Bug Report

### Describe the bug

After a recent update, I'm getting a duplicate function declaration error when trying to use the `NunjucksEnabledProvider` component. The application fails to compile with an error about `NunjucksEnabledProvider` being declared multiple times.

### Reproduction

```tsx
import { NunjucksEnabledProvider } from './nunjucks-enabled-context';

// Trying to use the provider
<NunjucksEnabledProvider disable={false}>
  <MyComponent />
</NunjucksEnabledProvider>
```

The code won't compile and throws an error about duplicate identifiers.

### Expected behavior

The provider should work as expected without any compilation errors. There should only be one declaration of `NunjucksEnabledProvider`.

### System Info
- TypeScript version: latest
- React version: 18.x

This seems to have started happening in the latest commit. The component was working fine before.

---
Repository: /testbed
