Hey, I need your help enforcing a security policy on our Kubernetes cluster configuration. I have a file at `/home/user/devsecops/pod_configs.csv` that lists pod configurations deployed in our cluster. Our policy requires that all pods must have `privileged` mode set to `false`. I need to generate a compliance violation report listing only the non-compliant pods.

The CSV file has the following columns (with a header row):
```
pod_name,namespace,image,privileged,run_as_root
```

I need you to:

1. Find all rows where the `privileged` column is `true`.
2. Write a report to `/home/user/devsecops/violations.txt` in the following **exact** format:

```
POLICY VIOLATION REPORT: privileged=true
=========================================
<namespace>/<pod_name>
<namespace>/<pod_name>
...
```

The entries must be sorted alphabetically (standard `sort` order). The header lines must appear exactly as shown above (including the `=` separator line which is exactly 41 `=` characters). Each violation entry is `<namespace>/<pod_name>` with no leading spaces or extra characters.

For example, if `nginx-proxy` in namespace `frontend` and `debug-shell` in namespace `kube-system` are both privileged, the file should look like:

```
POLICY VIOLATION REPORT: privileged=true
=========================================
frontend/nginx-proxy
kube-system/debug-shell
```

The file at `/home/user/devsecops/pod_configs.csv` already exists. Please generate the violations report now.
