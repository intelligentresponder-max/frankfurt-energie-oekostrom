import json

def calculate():
    verbrauch = 2500 
    try:
        with open('tarife.json', 'r') as f:
            data = json.load(f)
        
        print(f"--- Stromvergleich Frankfurt ({verbrauch} kWh) ---")
        for t in data['tarife']:
            preis = t['preise']['gp_euro_jahr'] + (verbrauch * t['preise']['ap_ct'] / 100)
            print(f"{t['anbieter']}: {preis:.2f} €/Jahr")
            
    except Exception as e:
        print(f"Fehler: {e}")

if __name__ == "__main__":
    calculate()
