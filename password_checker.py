import re

def score_password(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"\d", password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    return score

def evaluate_password(score):
    if score == 5:
        return "💪 Strong"
    elif score >= 3:
        return "⚠️ Medium"
    else:
        return "❌ Weak"

def main():
    password = input("Enter a password to check: ")
    score = score_password(password)
    strength = evaluate_password(score)
    print(f"\nPassword Score: {score}/5")
    print(f"Password Strength: {strength}")

if __name__ == "__main__":
    main()
