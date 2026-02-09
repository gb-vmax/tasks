# Bug Report

### Describe the bug

I'm experiencing an issue with the OS template tag where it's not returning values correctly anymore. When I try to use `{% os 'arch' %}` or `{% os 'cpus' %}` in my templates, nothing gets rendered or the values are missing.

### Reproduction

```
{% os 'arch' %}
```

Expected to see something like `x64` or `arm64`, but getting no output.

Also tried with cpus:
```
{% os 'cpus' %}
```

This used to work fine and would return CPU information, but now it's broken.

### Expected behavior

The template tag should return the architecture string when using 'arch' and CPU information when using 'cpus', just like it did before.

### System Info
- Insomnia version: latest
- OS: macOS

This seems to have broken recently, possibly after a recent update. The template tags were working fine previously but now they don't return anything.

---
Repository: /testbed
