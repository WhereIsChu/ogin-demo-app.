## 📄 docs/common_issues.md

### 1. Incorrect Username or Password
**Description**: Users enter credentials that do not match the stored values.

**Cause**: The `login.py` script checks against a hardcoded dictionary. If the username is missing or the password is incorrect, it returns "Invalid credentials" without further detail.

**Impact**: Users are not told whether the username or the password was incorrect.

---

### 2. Case Sensitivity
**Description**: The login function treats usernames and passwords as case-sensitive.

**Cause**: No normalization is applied to the input.

**Impact**: Users typing "Alice" instead of "alice" or "Password123" instead of "password123" will be rejected.

---

### 3. No Rate Limiting or Lockout
**Description**: Repeated failed login attempts are not restricted.

**Cause**: No logic exists to handle brute-force protection.

**Impact**: The system is vulnerable to password-guessing attacks.

---

### 4. Hardcoded Credentials
**Description**: Users are limited to two predefined accounts: alice and bob.

**Cause**: The user store is a fixed dictionary.

**Impact**: New users cannot sign up or be authenticated unless the code is changed.

---

### 5. No Error Logging
**Description**: Failures aren’t logged or reported.

**Cause**: No logging mechanism is used.

**Impact**: Support engineers have no way to trace or debug failed login attempts.


## 📄 docs/help_articles.md

### 🔐 Title: Troubleshooting Login Failures

**Symptoms**:
- Seeing "Invalid credentials" after entering username and password
- Unable to tell if it’s the username or password that’s incorrect

**Steps to Troubleshoot**:
1. Make sure your username is exactly "alice" or "bob" (case-sensitive)
2. Make sure your password matches exactly "password123" (for alice) or "secret" (for bob)
3. Avoid extra spaces or misspellings
4. Remember, usernames and passwords are case-sensitive
5. Try copying and pasting your credentials directly from a note to reduce typos

---

### 🛡️ Title: Understanding Case Sensitivity in Logins

**Symptoms**:
- Login fails even though you believe you entered the correct credentials

**Steps to Troubleshoot**:
1. Double-check capitalization: "Alice" ≠ "alice"
2. Passwords like "Password123" will not work if the correct value is "password123"
3. If unsure, try typing credentials in a plain text editor and verify case

---

### 🧱 Title: Why You Can’t Create a New Account

**Symptoms**:
- No option to sign up
- Always getting "Invalid credentials"

**Steps to Troubleshoot**:
1. Understand that this version only supports two users: alice and bob
2. Contact support if you need access with new credentials
3. Developers can expand the user dictionary in `login.py` to include more users

---

### 🛑 Title: Protecting Your Account from Brute Force

**Symptoms**:
- Concerned about multiple login attempts
- No notification after several failed logins

**Steps to Troubleshoot**:
1. Be cautious if others have access to your terminal or device
2. Ask developers to implement rate limiting or lockout features
3. Monitor terminal access logs if applicable


## 📄 docs/faq.md

### ❓ Frequently Asked Questions

**Q: What usernames are allowed?**  
A: Only "alice" and "bob" are supported in this version.

**Q: Is the login case-sensitive?**  
A: Yes. Both the username and password must match exactly.

**Q: I forgot my password. Can I reset it?**  
A: Not in this version. The credentials are hardcoded. Contact the developer to update the code.

**Q: Can I sign up for a new account?**  
A: No. This version has a static user dictionary. For new users, the script must be modified.

**Q: Why does it just say 'Invalid credentials' without details?**  
A: For security reasons, the script doesn't specify if it's the username or password that’s incorrect.

**Q: How do I make this more secure?**  
A: You should add hashing, logging, input validation, and rate limiting to the code.
