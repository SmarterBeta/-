"""Deterministic baseline scaffold for M1.1 validation."""


def render_status(user_name: str) -> str:
    """Return a deterministic readiness string for a non-empty user name."""
    cleaned_name = user_name.strip()
    if not cleaned_name:
        raise ValueError("user_name must be a non-empty string")
    return f"baseline-ready:{cleaned_name}"


if __name__ == "__main__":
    print(render_status("demo-user"))
