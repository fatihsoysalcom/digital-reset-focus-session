import time
import os
import random
import sys

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def simulate_distractions(duration_seconds=20):
    """Simulates a stream of digital notifications/distractions.
    The article describes this as 'digital chaos' and 'constant notifications'.
    """
    distractions = [
        "Yeni bir e-posta geldi! (New email arrived!)",
        "Sosyal medyada bir bildiriminiz var! (You have a social media notification!)",
        "Haberler: Son dakika gelişmesi! (News: Breaking development!)",
        "Uygulama güncellemesi mevcut. (App update available.)",
        "Arkadaşınız mesaj gönderdi. (Your friend sent a message.)",
        "Hatırlatıcı: Yapılacaklar listenizi kontrol edin. (Reminder: Check your to-do list.)",
        "Reklam: Harika bir teklif sizi bekliyor! (Ad: A great offer awaits you!)",
        "Oyun daveti: Hemen katılın! (Game invite: Join now!)",
    ]
    start_time = time.time()
    print("Dijital Kaos Simülasyonu Başlıyor... (Digital Chaos Simulation Starting...)")
    print("Sürekli gelen bildirimler ve dikkat dağıtıcılar... (Constant notifications and distractions...)")
    print("-" * 70)

    while time.time() - start_time < duration_seconds:
        print(f"[{time.strftime('%H:%M:%S')}] {random.choice(distractions)}")
        time.sleep(random.uniform(1, 3)) # Simulate irregular notification arrival
        sys.stdout.flush() # Ensure immediate output

    print("-" * 70)
    print("Dijital Kaos sona erdi. Şimdi bir 'RESET' zamanı! (Digital Chaos ended. Now it's time for a 'RESET'!) ")
    input("Devam etmek için Enter'a basın... (Press Enter to continue...)")

def perform_reset():
    """Performs a 'reset' by clearing the screen and preparing for focus.
    This represents the article's call to 'reset' our digital lives.
    """
    clear_screen()
    print("RESET: Dijital Gürültüyü Temizle (RESET: Clear Digital Noise)")
    print("Odaklanmaya Hazırlanılıyor... (Preparing to Focus...)")
    time.sleep(2)
    clear_screen()

def focus_session(duration_minutes=1):
    """Starts a focused work session, free from digital distractions.
    This illustrates 'returning to real values' and 'conscious use of technology'.
    """
    print(f"Odaklanma Zamanı! ({duration_minutes} dakika) (Focus Time! ({duration_minutes} minutes))")
    print("Şimdi önemli bir göreve odaklanın. Tüm dijital dikkat dağıtıcılar susturuldu.")
    print("(Now focus on an important task. All digital distractions are silenced.)")
    print("Bu süre zarfında başka hiçbir şeyle ilgilenmeyin. (Do not engage with anything else during this time.)")
    print("-" * 70)

    start_time = time.time()
    end_time = start_time + duration_minutes * 60

    while time.time() < end_time:
        remaining_seconds = int(end_time - time.time())
        minutes = remaining_seconds // 60
        seconds = remaining_seconds % 60
        # Update on the same line to show remaining time
        print(f"\rKalan süre: {minutes:02d}:{seconds:02d} (Remaining time: {minutes:02d}:{seconds:02d})", end="", flush=True)
        time.sleep(1)
    print("\n") # New line after timer finishes

    print("-" * 70)
    print("Odaklanma süresi sona erdi! (Focus session ended!)")
    print("Gerçek değerlerinize odaklandığınız için tebrikler. (Congratulations on focusing on your real values.)")
    input("Devam etmek için Enter'a basın... (Press Enter to continue...)")

def main():
    clear_screen()
    print("RESET: Dijital Kaostan Kurtulup Gerçek Değerlere Dönüş")
    print("-----------------------------------------------------")
    print("Bu program, dijital dikkat dağıtıcıları simüle eder ve ardından bir 'reset' ile odaklanma süresi sunar.")
    print("(This program simulates digital distractions and then offers a 'reset' followed by a focus session.)")
    input("Başlamak için Enter'a basın... (Press Enter to begin...)")

    # Step 1: Simulate the overwhelming digital chaos
    simulate_distractions(duration_seconds=20) # Shorter duration for demonstration

    # Step 2: Perform the 'reset' to clear the noise and prepare for focus
    perform_reset()

    # Step 3: Start a focus session to work on 'real values'
    focus_session(duration_minutes=1) # Shorter duration for demonstration

    clear_screen()
    print("Program sona erdi. Dijital yaşamınızda 'reset' düğmesine basmayı unutmayın!")
    print("(Program ended. Don't forget to press the 'reset' button in your digital life!)")
    print("Gerçekten değer verdiğiniz şeylere odaklanın. (Focus on what you truly value.)")

if __name__ == "__main__":
    main()
