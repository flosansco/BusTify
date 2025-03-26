import numpy as np
import matplotlib.pyplot as plt

class BEB_Vehicle:
    def __init__(self, params):
        # Paramètres du véhicule
        self.m = params['masse']                # kg
        self.Sf = params['surface_frontale']    # m2
        self.Cx = params['Cx']                  # -
        self.fr = params['fr']                  # -
        self.r_roue = params['rayon_roue']      # m
        self.eta_transmission = params['rendement_transmission']  # -
        self.Pmax_moteur = params['Pmax_moteur']  # W
        self.Cmax_moteur = params['Cmax_moteur']  # Nm
        self.battery_capacity = params['battery_capacity']  # kWh
        
        # Initialisation du SOC
        self.SOC_init = params.get('SOC_init', 100.0)
    
    def force_resistances(self, v, pente=0.0):
        g = 9.81
        rho_air = 1.225
        
        F_roulement = self.m * g * self.fr * np.cos(np.arctan(pente/100))
        F_pente = self.m * g * np.sin(np.arctan(pente/100))
        F_aero = 0.5 * rho_air * self.Cx * self.Sf * v**2
        
        return F_roulement + F_pente + F_aero
    
    def simulate_drive_cycle(self, temps, vitesse, pente=0.0):
        dt = np.diff(temps, prepend=temps[0])
        acceleration = np.gradient(vitesse, temps)
        
        # Forces et puissances
        F_traction = self.m * acceleration + self.force_resistances(vitesse, pente)
        couple_traction = F_traction * self.r_roue
        couple_traction = np.clip(couple_traction, -self.Cmax_moteur, self.Cmax_moteur)
        
        # Puissance demandée
        puissance_meca = F_traction * vitesse  # W
        puissance_elec = puissance_meca / self.eta_transmission  # W
        puissance_elec = np.clip(puissance_elec, -self.Pmax_moteur, self.Pmax_moteur)
        
        # Calcul SOC
        energie_pos = np.trapz(np.clip(puissance_elec, 0, None), temps) / 3600000  # kWh
        energie_recup = np.trapz(np.clip(puissance_elec, None, 0), temps) / 3600000  # kWh
        
        SOC_final = self.SOC_init - (energie_pos / self.battery_capacity) * 100
        
        # Courbes SOC instantané
        soc_profile = self.SOC_init - np.cumsum(np.clip(puissance_elec, 0, None) * dt) / 3600 / self.battery_capacity * 100
        
        return {
            'temps': temps,
            'vitesse': vitesse * 3.6,
            'puissance_elec': puissance_elec / 1000,
            'couple_traction': couple_traction,
            'soc_profile': soc_profile,
            'energie_pos': energie_pos,
            'energie_recup': energie_recup,
            'SOC_final': SOC_final
        }

# === Exemple de Simulation ===
params_vehicule = {
    'masse': 13000,
    'surface_frontale': 8.0,
    'Cx': 0.6,
    'fr': 0.0075,
    'rayon_roue': 0.5,
    'rendement_transmission': 0.95,
    'Pmax_moteur': 250000,
    'Cmax_moteur': 2000,
    'battery_capacity': 350,  # kWh
    'SOC_init': 100
}

bus = BEB_Vehicle(params_vehicule)

# === Cycle simplifié ===
temps = np.linspace(0, 1000, 1001)
vitesse = np.piecewise(temps, [temps < 300, (temps >= 300) & (temps < 600), temps >= 600],
                       [0, 15/3.6, 0])

results = bus.simulate_drive_cycle(temps, vitesse)

# === Affichage ===
plt.figure(figsize=(10, 8))

plt.subplot(3, 1, 1)
plt.plot(results['temps'], results['vitesse'], label='Vitesse (km/h)')
plt.ylabel('Vitesse (km/h)')
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(results['temps'], results['puissance_elec'], label='Puissance électrique (kW)', color='orange')
plt.ylabel('Puissance (kW)')
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(results['temps'], results['soc_profile'], label='SOC (%)', color='green')
plt.xlabel('Temps (s)')
plt.ylabel('SOC (%)')
plt.legend()

plt.tight_layout()
plt.show()

# Résultats de la simulation
print(f"Énergie consommée : {results['energie_pos']:.2f} kWh")
print(f"Énergie récupérée : {abs(results['energie_recup']):.2f} kWh")
print(f"SOC final : {results['SOC_final']:.2f} %")
