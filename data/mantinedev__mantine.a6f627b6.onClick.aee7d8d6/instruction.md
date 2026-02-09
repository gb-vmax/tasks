# Bug Report

### Describe the bug

When using the `Stepper` component with `allowStepSelect={false}`, clicking on a step still triggers the `onStepClick` callback. The `allowStepSelect` prop should prevent step selection entirely, but the callback is being invoked regardless of this setting.

### Reproduction

```jsx
import { Stepper } from '@mantine/core';

function Demo() {
  const [active, setActive] = useState(0);

  return (
    <Stepper 
      active={active} 
      allowStepSelect={false}
      onStepClick={(stepIndex) => {
        console.log('Step clicked:', stepIndex); // This shouldn't fire when allowStepSelect is false
        setActive(stepIndex);
      }}
    >
      <Stepper.Step label="Step 1" />
      <Stepper.Step label="Step 2" />
      <Stepper.Step label="Step 3" />
    </Stepper>
  );
}
```

### Expected behavior

When `allowStepSelect={false}`, clicking on any step should not trigger the `onStepClick` callback at all. The steps should be non-interactive and the callback should remain silent.

### Actual behavior

The `onStepClick` callback is being called even when `allowStepSelect` is set to `false`, allowing users to navigate between steps when they shouldn't be able to.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
