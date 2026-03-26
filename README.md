# 🧠 Learning Python

A self guide and exercises on my way to learning python.

---

# 📦 Python Naming Conventions (Quick Cheat Sheet)

| Item           | Convention              | Example                |
|----------------|-------------------------|------------------------|
| File / Module  | snake_case              | `user_service.py`      |
| Package        | lowercase               | `utils`                |
| Variable       | snake_case              | `user_name`            |
| Function       | snake_case              | `get_user()`           |
| Class          | PascalCase              | `UserService`          |
| Constant       | UPPER_CASE              | `MAX_RETRIES`          |
| Private method | `_method_name`          | `_validate()`          |
| Strong private | `__method_name`         | `__secret()`           |
| Boolean        | `is_/has_/can_/should_` | `is_active`            |
| Exception      | PascalCase + Error      | `UserNotFoundError`    |
| Test Files     | test_ + module_name     | `test_user_service.py` |
| Internal Modules      | _ + snake_case          | `_utils.py`    |

---

# 🥇 Example of Clean Python Code

```
MAX_LOGIN_ATTEMPTS = 5


class UserService:

    def __init__(self):
        self.user_count = 0

    def create_user(self, user_name: str):
        if self._is_valid_user(user_name):
            self.user_count += 1

    def _is_valid_user(self, user_name: str) -> bool:
        return len(user_name) > 3
```

---

# 🛠 Difference Between Private and Strongly Private

Python does not have real access modifiers like Java (private, protected).

Instead it uses conventions + name mangling.

## 🥊 Private (_variable)

Prefixing with a single underscore means:

`_internal_use`

Example:

```
class UserService:

    def __init__(self):
        self._user_count = 0

    def _validate_user(self):
        pass
```

Meaning:

"This is internal. Please don't use it outside the class."

But Python does not enforce it.
You can still access it:

```
service = UserService()
service._validate_user()
```

It’s just a developer warning.

## 🥊 Strongly Private (__variable)

Double underscore triggers name mangling.

Example:

```
class BankAccount:

    def __calculate_interest(self):
        pass
```

Python internally renames it to:

`_BankAccount__calculate_interest`

This prevents accidental access or overrides.

Example:

```
class Test:
    def __private(self):
        print("hidden")

t = Test()

t.__private()     # ❌ error
```

But this works:

`t._Test__private()`

Because of name mangling.

### 🚀 Why Strongly Private Exists

Main reason:

`Prevent subclass collisions`

Example problem without mangling:

```
class A:
    def _process(self):
        pass


class B(A):
    def _process(self):
        pass
```

Method accidentally overrides.

With `__process`, Python isolates it.

## 🥇 Summary

| Prefix       | Meaning                | Enforcement   |
| ------------ | ---------------------- | ------------- |
| `variable`   | Public                 | None          |
| `_variable`  | Private (internal use) | Convention    |
| `__variable` | Strongly private       | Name mangling |

## 🧠 Practical Advice (Used in Real Code)

Most production Python code uses:

```
_public_method()
_private_method()
```

and rarely uses `__double_underscore`.

Double underscore is mostly used in framework internals and advanced inheritance cases.

---