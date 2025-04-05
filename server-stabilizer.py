import time
import random
import sys

def log(message):
    timestamp = time.strftime("[%Y-%m-%d %H:%M:%S]")
    print(f"{timestamp} {message}")

def diagnose_issues():
    log("Analysoidaan järjestelmän epävakaus...")
    time.sleep(2)
    fake_issues = [
        "Ylikuormitettu prosessi: phantomd (PID 8392)",
        "Korkea muistinkäyttö: RAM 95%",
        "Verkkoyhteysviive havaittu DNS-palveluun",
        "Viallinen välimuisti löydetty palvelusta: cache.service",
        "Satunnainen bittihäiriö havaittu debug-ytimessä"
    ]
    issues_found = random.sample(fake_issues, k=random.randint(1, len(fake_issues)))
    for issue in issues_found:
        log(f"🔍 Havaittu ongelma: {issue}")
        time.sleep(1)
    return issues_found

def apply_fixes(issues):
    log("Aloitetaan korjaukset...")
    for issue in issues:
        action = f"Korjataan: {issue}"
        log(action)
        time.sleep(random.uniform(0.5, 1.5))
        log("✅ Korjaus valmis")
    log("Kaikki toimenpiteet suoritettu.")

def restart_services():
    services = ["web-server", "database", "dns-resolver"]
    log("Käynnistetään ydinkomponentit uudelleen...")
    for service in services:
        log(f"🔄 Käynnistetään {service}...")
        time.sleep(1)
        log(f"✅ {service} käynnistyi onnistuneesti")
    log("Palvelin toimii nyt vakaammin.")

def main():
    log("Palvelimen korjausapu käynnistetty.")
    issues = diagnose_issues()
    if not issues:
        log("Palvelin vaikuttaa vakaalta. Ei toimenpiteitä tarvittu.")
    else:
        apply_fixes(issues)
        restart_services()
    log("Korjausprosessi päättynyt.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        log("Keskeytetty käyttäjän toimesta.")
        sys.exit(1)

