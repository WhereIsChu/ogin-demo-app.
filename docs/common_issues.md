## 📄 docs/common_issues.md

### 1. Users Can't Log In with Correct Credentials
**Description**: Some users believe they're entering the right info but still see "Invalid credentials."

**Cause**: Hardcoded username/password pairs; case sensitivity.

**Impact**: Users get blocked if credentials don’t exactly match `"alice": "password123"` or `"bob": "secret"`.

---

### 2. Account Lockouts After Repeated Failed Logins
**Description**: Users are locked out after too many failed login attempts.

**Cause**: `max_login_attempts` is set to 10 in config.json.

**Impact**: Repeated failures result in temporary or permanent lockout.

---

### 3. Insecure Passwords Allowed
**Description**: Users may think short passwords are safe due to low minimum length.

**Cause**: `password_min_length` is set to 3.

**Impact**: Encourages poor password habits; higher security risk.

---

### 4. Session Timeout Confusion
**Description**: Users stay logged in longer than expected.

**Cause**: Session duration is set to 240 minutes (4 hours).

**Impact**: User may forget to log out or feel sessions are insecure.
