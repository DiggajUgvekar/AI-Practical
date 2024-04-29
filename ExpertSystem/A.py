class ExpertSystem:
    def __init__(self):
        self.knowledge_base = {
            'Engine': {
                'Symptoms': ['Engine misfires', 'Difficulty starting', 'Loss of power'],
                'Actions': 'Check spark plug, Check fuel system, Check ignition system'
            },
            'Brakes': {
                'Symptoms': ['Spongy brakes', 'Brake noise', 'Brake pedal feels soft'],
                'Actions': 'Check brake fluid level, Inspect brake pads, Bleed brakes'
            },
            'Tires': {
                'Symptoms': ['Uneven tire wear', 'Low tire pressure', 'Vibrations while riding'],
                'Actions': 'Check tire pressure, Check tire tread, Wheel balancing'
            }
            # Add more components and their symptoms/actions as needed
        }

    def diagnose_issue(self, symptom):
        for component, data in self.knowledge_base.items():
            if symptom in data['Symptoms']:
                return f"Possible issue with {component}: {data['Actions']}"
        return "Symptom not recognized. Please consult a professional mechanic."

# Example usage:
expert = ExpertSystem()
symptom = 'Vibrations while riding'
print(expert.diagnose_issue(symptom))
