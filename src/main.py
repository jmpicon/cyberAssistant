# main.py
import machine_learning_module
import data_analysis_module

def main():
    user_data = data_analysis_module.collect_user_data()
    threat_level = machine_learning_module.analyze_threats(user_data)
    recommendations = data_analysis_module.generate_recommendations(threat_level)
    print("Recomendaciones de Seguridad: ", recommendations)

if __name__ == "__main__":
    main()
