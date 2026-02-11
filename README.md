# DevSecOps Lab: Secure Pipeline

A production-ready DevSecOps pipeline demonstrating automated security testing in CI:
- ✅ **SAST** with Semgrep
- ✅ **SCA** with Trivy
- ✅ **DAST** with OWASP ZAP (baseline scan)
- ✅ **Secret scanning** (via code patterns)
- ✅ **Non-root containerized app**

All tests run **inside GitHub Actions** — no external infrastructure required.

## Vulnerable App
The `app/` directory contains a deliberately vulnerable Flask application with:
- SQL injection (simulated)
- Reflected XSS
- Hardcoded API secret

> ⚠️ This app is for **educational and pipeline testing purposes only**.

## How It Works
On every pull request:
1. The app is built in a secure Docker container (non-root user).
2. SAST scans source code for anti-patterns.
3. SCA checks dependencies for known CVEs.
4. DAST runs OWASP ZAP against the running app on `localhost`.
5. Pipeline fails if **high/critical** issues are found.

## Usage
Fork this repo and enable GitHub Actions. No setup needed.

## License
MIT © Lucas Tomioka