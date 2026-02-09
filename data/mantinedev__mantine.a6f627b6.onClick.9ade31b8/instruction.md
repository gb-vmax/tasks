# Bug Report

### Describe the bug

The Stepper component's step click behavior is inverted. Steps are clickable when `allowStepClick` is disabled, and not clickable when it should be enabled. This makes it impossible to navigate between steps by clicking on them when step selection is supposed to be allowed.

### Reproduction

```jsx
import { Stepper } from '@mantine/core';

function Demo() {
  const [active, setActive] = useState(0);

  return (
    <Stepper active={active} onStepClick={setActive}>
      <Stepper.Step label="Step 1">Content 1</Stepper.Step>
      <Stepper.Step label="Step 2">Content 2</Stepper.Step>
      <Stepper.Step label="Step 3">Content 3</Stepper.Step>
    </Stepper>
  );
}
```

Steps to reproduce:
1. Create a Stepper with `onStepClick` handler
2. Try clicking on different steps
3. Nothing happens - the steps don't respond to clicks

If you explicitly set `allowStepClick={false}`, then the steps become clickable (which is the opposite of what should happen).

### Expected behavior

When `onStepClick` is provided, clicking on steps should trigger the handler and allow navigation between steps. The `allowStepClick` prop should control whether steps are clickable, not invert the behavior.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
