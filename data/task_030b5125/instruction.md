Hey, I need your help with something quick. I'm deploying a set of microservice container artifacts to a staging environment and I need to verify their integrity before the deployment pipeline proceeds.

I have three microservice archives in the directory `/home/user/deploy/artifacts/`:
- `auth-service-2.1.4.tar.gz`
- `billing-service-1.8.0.tar.gz`
- `gateway-service-3.0.2.tar.gz`

**Step 1:** Generate a SHA256 checksum manifest file at `/home/user/deploy/checksums.sha256`. The file must contain one line per artifact in the standard `sha256sum` output format (i.e., the format that `sha256sum` produces natively — a 64-character hex digest, two spaces, then the filename with no directory prefix). The entries must appear in alphabetical order by filename (auth first, then billing, then gateway). The file must end with a newline.

**Step 2:** Verify all three checksums against the manifest file you just created, running the verification from the `/home/user/deploy/artifacts/` directory so that the filenames in the manifest resolve correctly. The verification command should exit with status 0 (all OK).

The final state I need is:
- `/home/user/deploy/checksums.sha256` exists and contains exactly 3 lines in alphabetical order by filename, each in the format: `<sha256hex>  <filename>` (64-char hex, two spaces, bare filename — no path prefix).
- The checksums in that file are correct for the actual file contents (i.e., `sha256sum --check` passes with no failures).

Can you do that for me?
