# Bug Report

### Describe the bug

The AsyncButton component appears to have a syntax error in its type definitions. When trying to use the component, TypeScript throws errors about unexpected tokens and malformed interface definitions.

### Reproduction

```tsx
import { AsyncButton } from './themed-button/async-button';

function MyComponent() {
  const handleClick = async () => {
    await someAsyncOperation();
  };

  return (
    <AsyncButton onClick={handleClick}>
      Click me
    </AsyncButton>
  );
}
```

When trying to compile or use this component, you'll get TypeScript errors about the AsyncButtonProps interface being malformed.

### Expected behavior

The AsyncButton component should compile without errors and accept an async onClick handler as a prop. The interface should be properly defined and the component should be usable in TypeScript projects.

### System Info
- Insomnia version: latest
- TypeScript version: 4.x+

---
Repository: /testbed
