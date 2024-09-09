from config.database import engine, Base
from models.user import User  # Assure-toi que le modèle User est importé
from models.Item import Item
from models.client import Client
from models.compt import Compte
from models.facturation import Facture
from models.facturationLigneItem import FacturationLigneItem
from models.freelancer import Freelancer
from models.LigneItem import LigneItem
from models.paiement import Paiement








# Créer toutes les tables (si elles n'existent pas encore)
Base.metadata.create_all(bind=engine)

print("Tables créées avec succès.")
