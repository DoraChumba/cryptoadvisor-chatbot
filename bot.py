# bot.py
from data.crypto_data import crypto_db
from utils.nlp_utils import preprocess

# Define intent keywords with synonyms
INTENT_KEYWORDS = {
    "trending_up": [
        "trend", "rise", "up", "grow", "go up", "rising", "upward", "bullish"
    ],
    "sustainability": [
        "sustain", "eco", "green", "environment", "planet", "carbon", "clean",
        "friendly", "earth", "climate", "greenest", "eco-friendly"
    ],
    "profitability": [
        "profit", "buy", "invest", "money", "rich", "growth", "purchase", "return",
        "returns", "long term", "investment", "gain"
    ],
    "energy_use": [
        "energy", "power", "use", "consume", "electricity", "kwh", "watt", "low power"
    ]
}

def detect_intent(tokens):
    """Detect user intent based on presence of keywords"""
    detected = set()
    for intent, keywords in INTENT_KEYWORDS.items():
        if any(word in tokens for word in keywords):
            detected.add(intent)
    return detected

def CryptoAdvisor():
    print("Hello, I’m CryptoAdvisor. How can I assist you with your cryptocurrency data and insights today?")
    
    while True:
        try:
            user_input = input("\nYou: ").strip().lower()

            if "exit" in user_input or "quit" in user_input:
                print("CryptoAdvisor:  Thank you for using CryptoAdvisor.Take care and see you soon")
                break

            # Preprocess user input
            tokens = preprocess(user_input)

            # Detect intent
            intents = detect_intent(tokens)

            if not intents:
                print("CryptoAdvisor: Not sure what you're asking. Try asking about trends, sustainability, or profitability.")
                continue

            # Respond based on intent
            if "trending_up" in intents:
                rising_cryptos = [name for name, data in crypto_db.items() if data["price_trend"] == "rising"]
                if rising_cryptos:
                    print(f"CryptoAdvisor: {', '.join(rising_cryptos)} is/are trending up right now! ")
                else:
                    print("CryptoAdvisor: Hmm, no cryptos are rising at the moment.")

            if "sustainability" in intents:
                recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
                score = crypto_db[recommend]["sustainability_score"] * 10
                print(f"CryptoAdvisor: Invest in {recommend}! It’s eco-friendly (score: {int(score)}/10) and has long-term potential!")

            if "profitability" in intents:
                profitable = [
                    name for name, data in crypto_db.items()
                    if data["price_trend"] == "rising" and data["market_cap"] == "high"
                ]
                if profitable:
                    print(f"CryptoAdvisor: {' and '.join(profitable)} are good picks for long-term growth. ")
                else:
                    print("CryptoAdvisor: Not seeing any high-market-cap cryptos currently on the rise. Try checking back later!")

            if "energy_use" in intents:
                low_energy = [name for name, data in crypto_db.items() if data["energy_use"] == "low"]
                if low_energy:
                    print(f"CryptoAdvisor: {', '.join(low_energy)} use(s) less energy — perfect for eco-conscious investors. ")
                else:
                    print("CryptoAdvisor: All cryptos here use some level of energy. Cardano is the most efficient so far!")

        except KeyboardInterrupt:
            print("\nCryptoAdvisor: Session ended abruptly. See you soon!")
            break

if __name__ == "__main__":
    CryptoAdvisor()