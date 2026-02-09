# Bug Report

### Describe the bug

I'm having an issue with environment updates in Insomnia. When I try to update an environment with a color value, it's throwing an error even though the color format looks correct to me.

### Reproduction

```js
const environment = {
  name: 'Production',
  color: '#FF5733',
  data: {}
};

// This throws an error now
updateEnvironment(environment, {
  color: 'red'
});
```

I was using named colors like 'red', 'blue', 'green' etc. for environment colors and it was working fine before. Now it's rejecting these values and requiring hex format.

### Expected behavior

Either the named colors should continue to work like before, or there should be clearer documentation about what color formats are accepted. The error message mentions hex colors, but I wasn't aware this was a requirement.

### Additional context

This seems to have started happening recently. I have a lot of environments configured with named colors and now I can't update any of them without changing all the color values to hex format first.

---
Repository: /testbed
