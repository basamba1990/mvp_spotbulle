from typing import Dict
from sklearn.cluster import KMeans
import numpy as np

class DISCService:
    def __init__(self):
        self.model = KMeans(n_clusters=4)
        self.labels = ["Dominance", "Influence", "Stabilité", "Conformité"]
    
    async def analyze_responses(self, responses: Dict[str, int]) -> Dict:
        try:
            # Convertir les réponses en tableau numpy
            response_array = np.array(list(responses.values())).reshape(1, -1)
            
            # Entraînement du modèle (à remplacer par un modèle pré-entraîné en production)
            self.model.fit(response_array)
            
            # Calcul des scores
            scores = {label: float(np.random.rand()) for label in self.labels}
            total = sum(scores.values())
            normalized = {k: round(v/total * 100, 1) for k, v in scores.items()}
            
            return {
                "type": self.labels[self.model.labels_[0]],
                "scores": normalized
            }
        except Exception as e:
            raise ValueError(f"Error analyzing DISC responses: {str(e)}")
