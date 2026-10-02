import subprocess


def run_test(username, password):
    result = subprocess.run(
        ["python", "secure_code.py"],
        input=f"{username}\n{password}\n",
        text=True,
        capture_output=True
    )
    return result.stdout.strip()


print("SECURITY TESTING")
print("=" * 30)

# Test 1: Correct credentials
result = run_test("admin", "admin123")
print("Test 1 - Correct credentials:", result)

# Test 2: Wrong password
result = run_test("admin", "wrong123")
print("Test 2 - Wrong password:", result)

# Test 3: Wrong username
result = run_test("testuser", "admin123")
print("Test 3 - Wrong username:", result)

print("=" * 30)
print("Security testing completed.")