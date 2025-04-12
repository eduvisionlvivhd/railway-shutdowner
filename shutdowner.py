import time
import subprocess

print("🕓 Чекаємо 4 хвилини перед виключенням Railway...")
time.sleep(240)  # 4 хв

print("⏹ Вимикаємо Railway контейнер...")
result = subprocess.run("railway down --yes", shell=True)
print("✅ Команда завершена з кодом:", result.returncode)
