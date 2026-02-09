# Bug Report

### Describe the bug

The PromptButton component appears to have duplicate code in the `handleClick` function after a recent update. There are two `handleClick` function definitions in the same scope, and the second one is incomplete/malformed. This causes a syntax error and the component fails to render.

### Reproduction

```tsx
import { PromptButton } from '@/ui/components/base/prompt-button';

// Try to use the PromptButton component
<PromptButton onClick={() => console.log('clicked')}>
  Delete
</PromptButton>
```

When attempting to use the PromptButton component, the application fails to compile due to a syntax error in the component file.

### Expected behavior

The PromptButton should render correctly and handle the confirmation flow when clicked (first click shows confirmation, second click triggers the action).

### Additional context

Looking at the component code, there seems to be a merge conflict or incomplete refactoring that left duplicate function definitions. The second `handleClick` function also tries to use `useRef` inside the function body which violates React hooks rules.

---
Repository: /testbed
