# Bug Report

### Describe the bug

I'm getting a syntax error when trying to use Mantine components. The application fails to compile with an error related to the `extend` method in the factory module.

### Reproduction

```tsx
import { Button } from '@mantine/core';

function App() {
  return <Button>Click me</Button>;
}
```

The code fails to compile immediately when importing any Mantine component.

### Expected behavior

Components should import and render without compilation errors. The `extend` method should be properly defined as a function property, not have inline implementation code.

### Error details

The compilation fails with a syntax error in `packages/@mantine/core/src/core/factory/factory.tsx`. It appears the `extend` property in the `ThemeExtend` interface has been changed from a function signature to an inline function implementation, which is not valid TypeScript syntax for interface definitions.

### System Info
- @mantine/core version: latest
- TypeScript version: 5.x
- Build tool: Vite/Webpack

---
Repository: /testbed
